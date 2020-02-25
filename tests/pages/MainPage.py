from .BasicPage import BasicPage
from selenium.webdriver.common.keys import Keys

class MainPage(BasicPage):
	redirect_error = 'body a[href="https://vk.com/"][style="position: absolute; left: 50%; top: 50%; margin: -265px -345px 0px; height: 530px; width: 690px;"]'
	
	btn_write_message = ".group_send_msg_status_block_title"
	block_input_message = "#mail_box_editable"
	btn_send_message = "#mail_box_send"
	block_input_add_news = "#post_field"
	btn_send_added_news = "#send_post"
 
 
	def redirect(self, url):			
		self.driver.get(url)
		self.wait_redirect(url)

	def write_message(self, text):
		elem = self.wait_render(self.btn_write_message)
		elem.click()
		elem = self.wait_render(self.block_input_message)
		elem.send_keys(text)
		elem = self.wait_render(self.btn_send_message)
		elem.click()
	 
	def write_post(self, text):
		elem = self.wait_render(self.block_input_add_news)
		elem.click()
		elem.send_keys(text)
		elem = self.wait_render(self.btn_send_added_news)
		elem.click()
	 