# tests/test_app.py
import unittest
import os
from dotenv import load_dotenv



load_dotenv(dotenv_path='.env.test')

from app import app

class AppTestCase(unittest.TestCase):
  def setUp(self):
      self.client = app.test_client()

  def test_home(self):
      response = self.client.get("/")
      assert response.status_code == 200
      html = response.get_data(as_text=True)
      assert "Maya Lekhi" in html
      #check for profile picture
      assert "./static/img/profile.jpg" in html

  def test_timeline(self):
      response = self.client.get("/api/timeline_post")
      assert response.status_code == 200
      assert response.is_json
      json = response.get_json()
      assert "timeline_post" in json

      self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "john@example.com",
                "content": "Hello world!",
            },
        )
      response = self.client.get("/api/timeline_post")
      assert response.status_code == 200
      assert response.is_json
      json = response.get_json()
      assert "timeline_post" in json
      post = json["timeline_post"][0]
      assert post["name"] == "John Doe"
      assert post["email"] == "john@example.com"
      assert post["content"] == "Hello world!"


  def test_malformed_timeline_post(self):
      # POST request missing name
      response = self.client.post("/api/timeline_post", data={
          "email": "john@example.com", "content": "Hello world, I'm John!"
      })
      assert response.status_code == 400
      html = response.get_data(as_text=True)
      assert "Invalid name" in html

      # POST request with empty content
      response = self.client.post("/api/timeline_post", data={
          "name": "John Doe", "email": "john@example.com", "content": ""
      })
      assert response.status_code == 400
      html = response.get_data(as_text=True)
      assert "Invalid content" in html

      # POST request with malformed email
      response = self.client.post("/api/timeline_post", data={
          "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"
      })
      assert response.status_code == 400
      html = response.get_data(as_text=True)
      assert "Invalid email" in html