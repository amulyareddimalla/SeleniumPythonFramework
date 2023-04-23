import psutil

def measure_performance(driver):
    # get initial CPU and memory usage
    initial_cpu_usage = psutil.cpu_percent()
    initial_memory_usage = psutil.virtual_memory().percent

    # measure the initial page load time
    initial_load_time = driver.execute_script(
        "return performance.timing.loadEventEnd - performance.timing.navigationStart")

    # get CPU and memory usage after initial load
    post_initial_cpu_usage = psutil.cpu_percent()
    post_initial_memory_usage = psutil.virtual_memory().percent

    # measure the products page load time
    products_load_time = driver.execute_script(
        "return performance.timing.loadEventEnd - performance.timing.navigationStart")

    # get CPU and memory usage after product load
    post_product_cpu_usage = psutil.cpu_percent()
    post_product_memory_usage = psutil.virtual_memory().percent

    # return a dictionary containing the performance metrics
    return {
        "initial_cpu_usage": initial_cpu_usage,
        "initial_memory_usage": initial_memory_usage,
        "initial_load_time": initial_load_time,
        "post_initial_cpu_usage": post_initial_cpu_usage,
        "post_initial_memory_usage": post_initial_memory_usage,
        "products_load_time": products_load_time,
        "post_product_cpu_usage": post_product_cpu_usage,
        "post_product_memory_usage": post_product_memory_usage
    }
