import math
from OpenSimula.Component import Component
from OpenSimula.Parameters import Parameter_options, Parameter_float, Parameter_float_list
from shapely.geometry import Polygon


class Surface(Component):
    def __init__(self, name, project):
        Component.__init__(self, name, project)
        # Parameters
        self.parameter("type").value = "Surface"
        self.parameter("description").value = "Building surface"
        self.add_parameter(Parameter_options(
            "shape", "RECTANGLE", ["RECTANGLE", "POLYGON"]))
        self.add_parameter(Parameter_float("width", 1, "m", min=0.0))
        self.add_parameter(Parameter_float("height", 1, "m", min=0.0))
        # Building Coordinate system
        self.add_parameter(Parameter_float_list(
            "ref_point", [0, 0, 0], "m", min=float("-inf")))
        self.add_parameter(Parameter_float_list(
            "x_polygon", [0, 10, 10, 0], "m", min=float("-inf")))
        self.add_parameter(Parameter_float_list(
            "y_polygon", [0, 0, 10, 10], "m", min=float("-inf")))
        self.add_parameter(Parameter_float(
            "azimuth", 0, "°", min=-180, max=180))  # Surface x vs Building x -> S: 0º, E: 90º, W: -90º, N: 180º
        self.add_parameter(Parameter_float(
            "altitude", 0, "°", min=-90, max=90))  # Surface y vs Building y -> vertical: 0º, facing up: 90º, facing down: -90º

    def check(self):
        errors = super().check()
        # Test if Polygon shape that x_polygon and y_polygon has the same size
        if self.parameter("shape").value == "POLYGON":
            if len(self.parameter("x_polygon").value) != len(self.parameter("y_polygon").value):
                errors.append(
                    f"Error: {self.parameter('name').value}, x_polygo and y_polygon must have the same size."
                )
        return errors

    @property
    def area(self):
        if (self.parameter("shape").value == "RECTANGLE"):
            return self.parameter("width").value * self.parameter("height").value
        elif (self.parameter("shape").value == "POLYGON"):
            polygon = []
            n = len(self.parameter("x_polygon").value)
            for i in range(0, n):
                polygon.append([self.parameter("x_polygon").value[i],
                               self.parameter("y_polygon").value[i]])
            return Polygon(polygon).area

    def orientation_angle(self, angle, side):  # exterior normal vector
        if angle == "azimuth":
            azi_building = self.building().parameter("azimuth").value
            az = self.parameter("azimuth").value + azi_building
            if side == 0:
                return az
            elif side == 1:
                if az > 0:
                    return az-180
                else:
                    return az+180
        elif angle == "altitude":
            alt = self.parameter("altitude").value
            if side == 0:
                return alt
            elif side == 1:
                return -alt

    def radiant_property(self, prop, radiation_type, side, theta=0):
        """It maus be redefined by child classes

        Args:
            prop (_type_): _description_
            radiation_type (_type_): _description_
            side (_type_): _description_

        Returns:
            _type_: _description_
        """
        return 0

    def is_virtual(self):
        return False

    def get_pyvista_polygon(self, coordinate_system="building"):
        v1 = self.parameter("ref_point").value
        az = math.radians(self.parameter("azimuth").value)
        alt = math.radians(self.parameter("altitude").value)
        if (self.parameter("shape").value == "RECTANGLE"):
            w = self.parameter("width").value
            h = self.parameter("height").value
            polygon2D = [[0, 0], [w, 0], [w, h], [0, h]]
        elif (self.parameter("shape").value == "POLYGON"):
            polygon2D = []
            n = len(self.parameter("x_polygon").value)
            for i in range(0, n):
                polygon2D.append([self.parameter("x_polygon").value[i],
                                  self.parameter("y_polygon").value[i]])
        polygon3D = []
        for vertex in polygon2D:
            v_loc = [v1[0]+vertex[0]*math.cos(az)-vertex[1]*math.sin(alt)*math.sin(az),
                     v1[1]+vertex[0] *
                     math.sin(az)+vertex[1] *
                     math.sin(alt)*math.cos(az),
                     v1[2]+vertex[1]*math.cos(alt)]
            if (coordinate_system == "global"):
                az_b = math.radians(self.building().parameter("azimuth").value)
                v_loc = [v_loc[0]*math.cos(az_b)-v_loc[1]*math.sin(az_b),
                         v_loc[0]*math.sin(az_b)+v_loc[1]*math.cos(az_b),
                         v_loc[2]]
            polygon3D.append(v_loc)
        return polygon3D
