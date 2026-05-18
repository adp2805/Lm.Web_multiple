#base_page este un fisier care contine o clasa in interiorul careia vom defini metode ce vor fi folosite in mai multe
# locuri, vor fi folosite in mai multe fisiere de steps cu diverse inputuri si care nu ar avea sens sa fie redefinite
# de multe ori in fisierele steps

#
from browser import Browser


class Base_page(Browser):
    def insert_input(self,input_value,element):
        self.driverObject.find_element(*element).send_keys(input_value)

    def find_elements(self,element):
        self.driverObject.find_elements(*element)

    def click_button(self,element):
        self.driverObject.find_element(*element).click()
        # self.driverObject.find_element(*element).click()

    def delete_input(self,element):
        self.driverObject.find_element(*element).clear()

    # #check any save err
    # def check_err(self,element):
    #     errors = self.driverObject.find_elements(*element)
    #     assert len(errors) == 0, f'Eroare detectata pe pagina: {errors[0].text if errors else  "Eroare necunoscuta"}'
        # if len(errors)>0:
        #     error_text = errors[0].text
        #     print(f'Warning!!! You have met an error here:{error_text}')
        #     return True
        # return False
    def verify_err_msg(self,err,element):
        actual_error_message = self.driverObject.find_element(*element).text
        err = "Procedure or function edsp_LM_GetNbAllowedTerminalsPerType has too many arguments specified."
        assert err == actual_error_message,f"Expected error message{err} is different from{actual_error_message}"


    def verify_err_msg_outline(self,err,element):
        actual_error_message = self.driverObject.find_element(*element).text
        assert  err == actual_error_message, f"Expected error message:{err} is different from {actual_error_message}"


    def verify_value(self,value_regional_center,value_retailer):
        assert int(value_retailer) <= int(value_regional_center),f"Err: Retailer limit{value_retailer} is higher than\
        regional center limit {value_regional_center} limit"



