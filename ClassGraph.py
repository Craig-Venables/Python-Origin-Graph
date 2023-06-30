import originpro as op
import ClassEquations as ce
import file_managment as fm

class plot_graph:
    """
    Class for all functions for data manipulation

    voltage_data = Voltage data | type: int
    current_data = Current data | type: int
    directory_path = working directory path | type: str
    filename = filename of current file | type: str
    graph_template_folder = Area graph template | type: str
    template_name = template use to plot the graph | type: str
    distance = Distance between electrodes default 100E-9 | type: int
    area = Area between electrodes default 100E-6 | type: int
    save_image = Save images of graphs in directory default = false | type: boolean
    """

    def __init__(self, voltage_data, current_data, directory_path,\
        filename, graph_template_folder, template_name = 'Electron_transport_Final.otpu', \
                 distance=100E-9, area=100E-6, save_image = False )-> None:

        self.v_data = voltage_data
        self.c_data = current_data
        self.d_path = directory_path
        self.fn = filename
        self.g_temp_folder = graph_template_folder
        self.temp_name = template_name
        self.area = area
        self.distance = distance
        self.save_img = save_image

    # start an instance of this the classes needed
        self.func = ce.functions
        self.fm = fm.directory


    def plot_into_workbook(self):
        # give the file path of the temple.ogwu
        working_file = self.g_temp_folder + self.temp_name
        wks = op.load_book(working_file)[0]  # from user file folder

        # Put array into workbook
        wks.from_list(0, self.v_data, 'Voltage')
        wks.from_list(1, self.c_data, 'Current')

        # fixes name issue, sets names as it's broken in templates, *reportedly fixed now
        wksn = op.find_book()  # Changes workbook name
        wksn.lname = f"{self.fn}"
        wks.plot_cloneable(self.g_temp_folder + f"{self.fn}" )
        gp = op.find_graph() # changes graph name
        gp.lname = wksn.lname # longname
        #gp.name = wks.name # short name



    def plot_origin_using_python(self):
        # This works only for my use case, please ignore

        wks = op.new_book('w', lname=f"{self.fn}", hidden=False)[0]
        #check this works
        abs_current = self.func.absolute_val(self.c_data)

        # plot first 3 voltage current and abs(current)
        wks.from_list(0, self.v_data, 'Voltage', units='V')
        wks.from_list(1, self.c_data, 'Current', units='A')
        wks.from_list(2, abs_current, 'Abs Current')

        # find  positive values for data using functions "rpv"
        voltage_data_positive, current_data_positive = self.func.filter_positive_values(self.v_data, self.c_data)

        # run data through equations for positive values.
        current_density_p = self.func.current_density_eq(voltage_data_positive, current_data_positive, self.area, self.distance)
        electric_field_p = self.func.electric_field_eq(voltage_data_positive, self.distance)
        current_over_voltage_p = self.func.current_over_voltage_eq(voltage_data_positive, current_data_positive)
        voltage_to_the_half_p = self.func.voltage_to_the_half_eq(voltage_data_positive)

        # get positive values and plot for positive regions only
        wks.from_list(3, current_density_p, 'Current Density', units='A/cm^2')
        wks.from_list(4, electric_field_p, 'Electric Field' , units='V/cm')
        wks.from_list(5, current_over_voltage_p, 'Current/Voltage', units='A/V')
        wks.from_list(6, voltage_to_the_half_p, 'Voltage^1/2', units='V^1/2')

        # find negative values for data using functions "rpv" and "equations"
        voltage_data_negative, current_data_negative = self.func.filter_negative_values(self.v_data, self.c_data)

        # run data through equations for negative values.
        current_density_n = self.func.current_density_eq(voltage_data_negative, current_data_negative, self.area, self.distance)
        electric_field_n = self.func.electric_field_eq(voltage_data_negative, self.distance)
        current_over_voltage_n = self.func.current_over_voltage_eq(voltage_data_negative, current_data_negative)
        voltage_to_the_half_n = self.func.voltage_to_the_half_eq(voltage_data_negative)

        # get positive values and plot for positive regions only
        wks.from_list(7, self.func.absolute_val(voltage_data_negative), 'abs(Voltage)', units='V')
        wks.from_list(8, self.func.absolute_val(current_data_negative), 'abs(Current)', units='A')
        wks.from_list(9, self.func.absolute_val(current_density_n), 'abs(Current Density)', units='A/cm^2')
        wks.from_list(10, self.func.absolute_val(electric_field_n), 'abs(Electric Field)', units='V/cm')
        wks.from_list(11, self.func.absolute_val(current_over_voltage_n), 'abs(Current/Voltage)', units='A/v')
        wks.from_list(12, self.func.absolute_val(voltage_to_the_half_n), 'abs(Voltage^1/2)', units='V^1/2')

        # plots the graph using template provided, must be a clonable template
        electron_transport = self.g_temp_folder + 'Electron_transport_Final.otpu'
        iv_log = self.g_temp_folder + 'LOG+IV_v3.otpu'

        if not self.save_img == True:
            wks.plot_cloneable(electron_transport)
        else:
            wks.plot_cloneable(iv_log)

        # Fix short and long names of files
        wks.lname= f"{self.fn}"
        gp = op.find_graph()
        gp.lname = wks.lname
        gp.name = wks.name

    def plot_transport_and_save(self):
        check_if_folder_exists(self.d_path, 'Exported Graphs png (Transport)')
        g = op.find_graph()
        filename_ext = f"{self.fn}" + '.png'
        exported_path = self.d_path + '\\Exported Graphs png (Transport)'
        g.save_fig(str(exported_path) + '\\' + f"{filename_ext}")
        print("Transport image saved")

    def plot_iv_log_and_save(self):
        check_if_folder_exists(self.d_path, 'Exported Graphs png (iv_log)')
        g = op.find_graph()
        filename_ext = f"{self.fn}" + '.png'
        exported_path = self.d_path + '\\Exported Graphs png (iv_log)'
        g.save_fig(str(exported_path) + '\\' + f"{filename_ext}")
        # , width=500
        print ("IV LOG image saved")

    def tile_all_windows(self):
        if self == True:
            op.lt_exec('win-s T')





