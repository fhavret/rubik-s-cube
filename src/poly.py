from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import proj3d
from numpy import cos, sin
import numpy as np

class Poly3DCollection(PolyCollection):
    """
    A collection of 3D polygons.
    """

    def __init__(self, verts, *args, zsort=True, **kwargs):
        """
        Create a Poly3DCollection.
        *verts* should contain 3D coordinates.
        Keyword arguments:
        zsort, see set_zsort for options.
        Note that this class does a bit of magic with the _facecolors
        and _edgecolors properties.
        """
        super().__init__(verts, *args, **kwargs)
        # adding these two lines
        self.verts = verts
        self.facecolors = kwargs['facecolors']
        ########################
        self.set_zsort(zsort)
        self._codes3d = None

    _zsort_functions = {
        'average': np.average,
        'min': np.min,
        'max': np.max,
    }

    def set_zsort(self, zsort):
        """
        Sets the calculation method for the z-order.
        Parameters
        ----------
        zsort : bool or {'average', 'min', 'max'}
            For 'average', 'min', 'max' the z-order is determined by applying
            the function to the z-coordinates of the vertices in the viewer's
            coordinate system. *True* is equivalent to 'average'.
        """

        if zsort is True:
            zsort = 'average'

        if zsort is not False:
            if zsort in self._zsort_functions:
                zsortfunc = self._zsort_functions[zsort]
            else:
                return False
        else:
            zsortfunc = None

        self._zsort = zsort
        self._sort_zpos = None
        self._zsortfunc = zsortfunc
        self.stale = True

    def get_vector(self, segments3d):
        """Optimize points for projection."""
        si = 0
        ei = 0
        segis = []
        points = []
        for p in segments3d:
            points.extend(p)
            ei = si + len(p)
            segis.append((si, ei))
            si = ei

        if len(segments3d):
            xs, ys, zs = zip(*points)
        else :
            # We need this so that we can skip the bad unpacking from zip()
            xs, ys, zs = [], [], []

        ones = np.ones(len(xs))
        self._vec = np.array([xs, ys, zs, ones])
        self._segis = segis

    def set_verts(self, verts, closed=True):
        """Set 3D vertices."""
        self.get_vector(verts)
        # 2D verts will be updated at draw time
        PolyCollection.set_verts(self, [], False)
        self._closed = closed

    def set_verts_and_codes(self, verts, codes):
        """Sets 3D vertices with path codes."""
        # set vertices with closed=False to prevent PolyCollection from
        # setting path codes
        self.set_verts(verts, closed=False)
        # and set our own codes instead.
        self._codes3d = codes

    def set_3d_properties(self):
        # Force the collection to initialize the face and edgecolors
        # just in case it is a scalarmappable with a colormap.
        self.update_scalarmappable()
        self._sort_zpos = None
        self.set_zsort(True)
        self._facecolors3d = PolyCollection.get_facecolor(self)
        self._edgecolors3d = PolyCollection.get_edgecolor(self)
        self._alpha3d = PolyCollection.get_alpha(self)
        self.stale = True

    def set_sort_zpos(self,val):
        """Set the position to use for z-sorting."""
        self._sort_zpos = val
        self.stale = True

    def do_3d_projection(self, renderer):
        """
        Perform the 3D projection for this object.
        """
        # FIXME: This may no longer be needed?
        if self._A is not None:
            self.update_scalarmappable()
            self._facecolors3d = self._facecolors

        txs, tys, tzs = proj3d.proj_transform_vec(self._vec, renderer.M)
        xyzlist = [(txs[si:ei], tys[si:ei], tzs[si:ei])
                   for si, ei in self._segis]

        # This extra fuss is to re-order face / edge colors
        cface = self._facecolors3d
        cedge = self._edgecolors3d
        if len(cface) != len(xyzlist):
            cface = cface.repeat(len(xyzlist), axis=0)
        if len(cedge) != len(xyzlist):
            if len(cedge) == 0:
                cedge = cface
            else:
                cedge = cedge.repeat(len(xyzlist), axis=0)

        # if required sort by depth (furthest drawn first)
        if self._zsort:
            z_segments_2d = sorted(
                ((self._zsortfunc(zs), np.column_stack([xs, ys]), fc, ec, idx)
                 for idx, ((xs, ys, zs), fc, ec)
                 in enumerate(zip(xyzlist, cface, cedge))),
                key=lambda x: x[0], reverse=True)
        else:
            raise ValueError("whoops")

        segments_2d = [s for z, s, fc, ec, idx in z_segments_2d]
        if self._codes3d is not None:
            codes = [self._codes3d[idx] for z, s, fc, ec, idx in z_segments_2d]
            PolyCollection.set_verts_and_codes(self, segments_2d, codes)
        else:
            PolyCollection.set_verts(self, segments_2d, self._closed)

        self._facecolors2d = [fc for z, s, fc, ec, idx in z_segments_2d]
        if len(self._edgecolors3d) == len(cface):
            self._edgecolors2d = [ec for z, s, fc, ec, idx in z_segments_2d]
        else:
            self._edgecolors2d = self._edgecolors3d

        # Return zorder value
        if self._sort_zpos is not None:
            zvec = np.array([[0], [0], [self._sort_zpos], [1]])
            ztrans = proj3d.proj_transform_vec(zvec, renderer.M)
            return ztrans[2][0]
        elif tzs.size > 0 :
            # FIXME: Some results still don't look quite right.
            #        In particular, examine contourf3d_demo2.py
            #        with az = -54 and elev = -45.
            return np.min(tzs)
        else :
            return np.nan

    def set_facecolor(self, colors):
        PolyCollection.set_facecolor(self, colors)
        self._facecolors3d = PolyCollection.get_facecolor(self)

    def set_edgecolor(self, colors):
        PolyCollection.set_edgecolor(self, colors)
        self._edgecolors3d = PolyCollection.get_edgecolor(self)

    def set_alpha(self, alpha):
        """
        Set the alpha transparencies of the collection.  *alpha* must be
        a float or *None*.
        .. ACCEPTS: float or None
        """
        if alpha is not None:
            try:
                float(alpha)
            except TypeError:
                raise TypeError('alpha must be a float or None')
        artist.Artist.set_alpha(self, alpha)
        try:
            self._facecolors = mcolors.to_rgba_array(
                self._facecolors3d, self._alpha)
        except (AttributeError, TypeError, IndexError):
            pass
        try:
            self._edgecolors = mcolors.to_rgba_array(
                    self._edgecolors3d, self._alpha)
        except (AttributeError, TypeError, IndexError):
            pass
        self.stale = True

    def get_facecolor(self):
        return self._facecolors2d

    def get_edgecolor(self):
        return self._edgecolors2d

    def translate(self, dx, dy, dz):
        self.verts = list(map(lambda x: (list(map(lambda y: (y[0]+dx,
                                                             y[1]+dy,
                                                             y[2]+dz),
                                        x))),
                             self.verts))

    def rotate_xy(self, angle):
        cos_angle = cos(angle)
        sin_angle = sin(angle)
        self.verts = list(map(lambda x: (list(map(lambda y: (y[0]*cos_angle - y[1]*sin_angle,
                                                             y[1]*cos_angle + y[0]*sin_angle,
                                                             y[2]),
                                             x))),
                             self.verts))

    def rotate_xz(self, angle):
        cos_angle = cos(angle)
        sin_angle = sin(angle)
        self.verts = list(map(lambda x: (list(map(lambda y: (y[0]*cos_angle - y[2]*sin_angle,
                                                             y[1],
                                                             y[2]*cos_angle + y[0]*sin_angle),
                                             x))),
                             self.verts))

    def rotate_yz(self, angle):
        cos_angle = cos(angle)
        sin_angle = sin(angle)
        self.verts = list(map(lambda x: (list(map(lambda y: (y[0],
                                                             y[1]*cos_angle - y[2]*sin_angle,
                                                             y[2]*cos_angle + y[1]*sin_angle),
                                             x))),
                             self.verts))

    def rotate(self, x, y, z, angle):
        if x == 0:
            self.translate(0, -y, -z)
            self.rotate_yz(angle)
            self.translate(0, y, z)
        elif y == 0:
            self.translate(-x, 0, -z)
            self.rotate_xz(angle)
            self.translate(x, 0, z)
        else:
            self.translate(-x, -y, 0)
            self.rotate_xy(angle)
            self.translate(x, y, 0)

        self.__init__(self.verts, facecolors=self.facecolors, edgecolor='#000000')
