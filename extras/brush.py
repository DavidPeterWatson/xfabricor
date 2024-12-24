class Brush:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.brush_movement = float(config.get('brush_movement') or 20)
        self.brush_shift = float(config.get('brush_shift') or 10)
        self.brush_length = float(config.get('brush_length') or 80)
        self.brush_x_pos = float(config.get('brush_x_pos') or 0)
        self.brush_y_pos = float(config.get('brush_y_pos') or 100)
        self.safe_z_pos_for_brush = float(config.get('safe_z_pos_for_brush') or 30)
        self.printer.add_object('brush', self)


def load_config(config):
    return Brush(config)
