from .BasicPage import BasicPage
from selenium.webdriver.common.keys import Keys

class MainPage(BasicPage):
	redirect_error = 'body a[href="https://vk.com/"][style="position: absolute; left: 50%; top: 50%; margin: -265px -345px 0px; height: 530px; width: 690px;"]'
	
	btn_write_message = ".group_send_msg_status_block_title"
	block_input_message = "#mail_box_editable"
	btn_send_message = "#mail_box_send"
	block_input_add_post = "#post_field"
	btn_send_added_news = "#send_post"
 
	side_action_menu = "#narrow_column .page_action_menu_groups"
 
	counter_messages = 0
	counter_posts = 0
 
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
		self.counter_messages += 1
	 
	def write_post(self, text):
		elem = self.wait_render(self.block_input_add_post)
		elem.click()
		elem.send_keys(text)
		elem = self.wait_render(self.btn_send_added_news)
		elem.click()
		self.counter_posts += 1
	
	def write_smart_advertising(self, post_text, message_text):
		self.wait_render(self.side_action_menu)
		block_post = self.driver.find_elements_by_css_selector(self.block_input_add_post)
		block_message = self.driver.find_elements_by_css_selector(self.block_input_message)
		if block_post:
			self.write_post(post_text)
		elif block_message:
			self.write_message(message_text)
	 
	def show_statistick(self):
	 print(f'Statistick: \nMessages: {self.counter_messages}\nPosts: {self.counter_posts}\n') 