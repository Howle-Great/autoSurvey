from .BasicPage import BasicPage
from selenium.webdriver.common.keys import Keys

class MainPage(BasicPage):
	btn_write_message = ".group_send_msg_status_block_title"
	block_input_message = "#mail_box_editable"
	btn_send_message = "#mail_box_send"

	def write_message(self, text):
		elem = self.wait_render(self.btn_write_message)
		elem.click()
		elem = self.wait_render(self.block_input_message)
		elem.send_keys(text)
		elem = self.wait_render(self.btn_send_message)
		elem.click()
	 
	 