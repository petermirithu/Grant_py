from django.test import TestCase
from .models import projo_post,profile,reviews,preference,User
import datetime as dt

class projectTestCase(TestCase):
  '''
  class containing test cases for all function under projo_post class
  '''
  def setUp(self):
    self.user_pyra=User(username='pyra',password='5678bn',email='pyra_@yahoo.com')        
    self.user_pyra.save()

    self.post1=projo_post(title='instagram',landing_page_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',live_link='http://instagram.com',description='its an app giving people a chance to post pitures',posted_by=self.user_pyra,posted_on=dt,design=3,usability=7,content=5,total=15)
    self.post1.save()

    self.post2=projo_post(title='facebook',landing_page_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',live_link='http://instagram.com',description='its an app giving people a chance to post pitures',posted_by=self.user_pyra,posted_on=dt,design=8,usability=6,content=9,total=23)
    self.post2.save()

  def tearDown(self):
    User.objects.all().delete()
    projo_post.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.user_pyra,User))  
    self.assertTrue(isinstance(self.post1, projo_post))  
    self.assertTrue(isinstance(self.post2, projo_post))  

  def test_save_post(self):
    '''
    test case to save a new post
    '''
    self.post1.save_post()
    self.post2.save_post()
    posts=projo_post.objects.all()
    self.assertTrue(len(posts)==2)  

  def test_delete_post(self):
    '''
    test case to test on deleting a post
    '''
    self.post1.save_post()
    self.post2.save_post()
    found=projo_post.objects.get(title=self.post2.title)
    found.delete_post()
    posts=projo_post.objects.all()
    self.assertEqual(len(posts),1) 

  def test_get_all_posts(self):
    '''
    test case to test on getting all projects/posts
    '''
    self.post1.save_post()
    self.post2.save_post()
    posts=projo_post.get_all_posts()
    self.assertEqual(len(posts),2)

  def test_get_single_post(self):
    '''
    test case to test on getting a single post
    '''
    self.post1.save_post()
    self.post2.save_post()
    foundpost=projo_post.get_single_post(self.post2.id)
    self.assertTrue(self.post2.title==foundpost.title)

  def test_get_user_posts(self):
    '''
    test case to get all posts posted by one user
    '''
    self.user_pyra.save()
    self.post1.save_post()
    self.post2.save_post()
    userposts=projo_post.get_user_posts(self.user_pyra.id)
    self.assertTrue(len(userposts)==2)

  def test_winner_post(self):
    '''
    test case to find post with highest rating
    '''
    self.post1.save_post()
    self.post2.save_post()
    winnerpost=projo_post.winner_project()
    self.assertTrue(winnerpost.total==23)

  def test_search_project(self):
    '''
    test case to test on searching for projects
    '''
    self.post1.save_post()
    self.post2.save_post()
    found=projo_post.search_project('facebook')
    self.assertEqual(len(found),1)

class preferenceTestCase(TestCase):
  '''
  class that contains test cases for functions under preference model
  '''
  def setUp(self):
    self.user_pyra=User(username='pyra',password='5678bn',email='pyra_@yahoo.com')        
    self.user_pyra.save()

    self.post1=projo_post(title='instagram',landing_page_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',live_link='http://instagram.com',description='its an app giving people a chance to post pitures',posted_by=self.user_pyra,posted_on=dt,design=3,usability=7,content=5,total=15)
    self.post1.save()

    self.rater1=preference(user=self.user_pyra,post=self.post1,design=0,usability=0,content=0)    
    self.rater2=preference(user=self.user_pyra,post=self.post1,design=0,usability=0,content=0)    

  def tearDown(self):
    User.objects.all().delete()
    projo_post.objects.all().delete()
    preference.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.rater1, preference))
    self.assertTrue(isinstance(self.rater2, preference))

  def test_get_raters(self):
    '''
    test case to get users who have rated a post
    '''
    self.user_pyra.save()
    self.post1.save()

    self.rater1.save()
    self.rater2.save()

    raters=preference.get_rater_users(self.post1.id)

    self.assertEqual(len(raters),2)

class reviewsTestCase(TestCase):
  '''
  class that contains test cases for all function under review model
  '''
  def setUp(self):
    self.user_pyra=User(username='pyra',password='5678bn',email='pyra_@yahoo.com')        
    self.user_pyra.save()

    self.post1=projo_post(title='instagram',landing_page_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',live_link='http://instagram.com',description='its an app giving people a chance to post pitures',posted_by=self.user_pyra,posted_on=dt,design=3,usability=7,content=5,total=15)
    self.post1.save()

    self.review1=reviews(body='I like the app',projo_id=self.post1,posted_by=self.user_pyra,posted_on=dt)
    self.review2=reviews(body='Dope one',projo_id=self.post1,posted_by=self.user_pyra,posted_on=dt)

  def test_instance(self):
    self.assertTrue(isinstance(self.review1, reviews))
    self.assertTrue(isinstance(self.review2, reviews))

  def tearDown(self):
    User.objects.all().delete()
    projo_post.objects.all().delete()
    reviews.objects.all().delete()

  def test_get_post_reviews(self):
    '''
    test case to get all review for a projects/post
    '''    
    self.post1.save()
    self.review1.save()
    self.review2.save()

    found=reviews.project_reviews(self.post1.id)
    self.assertEqual(len(found),2)


class profileTestcase(TestCase):
  '''
  class containing test cases for all function under profile model
  '''
  def setUp(self):
    self.user_pyra=User(username='pyra',password='5678bn',email='pyra_@yahoo.com')        
    self.user_pyra.save()

    self.profile_pyra=profile(user=self.user_pyra ,bio='Software developer',profile_pic='https://ucarecdn.com/ff373002-7443-47bf-8007-747b9fe7fc95/',contact='0790476167',git_name='petermirithu')        
    # self.profile_pyra.save()
    
  def tearDown(self):
    User.objects.all().delete()
    profile.objects.all().delete()
    
  def test_instance(self):
    self.assertTrue(isinstance(self.user_pyra, User))
    self.assertTrue(isinstance(self.profile_pyra, profile))

    
  # def test_save(self):      
  #   self.user_pyra.save()      
  #   self.pyra.save_profile()
  #   profiles=profiles.objects.all()
  #   self.assertTrue(len(profiles)==1)











    

    











