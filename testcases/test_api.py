from APImethods.delMethod import DeleteMethod
from APImethods.getMethod import GetMethod
from APImethods.postMethod import PostMethod
from APImethods.putMethod import PutMethod

def test_api_methods():
    # Create objects of each class
    get = GetMethod()
    put = PutMethod()
    post = PostMethod()
    delete = DeleteMethod()

    # Call APImethods on each object
    get.get_data()
    put.update_data()
    post.post_data()
    delete.delete_data()
