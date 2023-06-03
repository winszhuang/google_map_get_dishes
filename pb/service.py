import grpc
import pb.crawl_pb2 as pb2
import pb.crawl_pb2_grpc as pb2_grpc
from spider.spider import DishesSpider

from concurrent import futures

driver_path = "D:/chromedriver_win32/chromedriver.exe"
dishesSpider = DishesSpider(driver_path)


class Spider(pb2_grpc.SpiderServicer):

    def CrawlDishesFromGoogleMap(self, request, context):
        googleMapUrl = request.googleMapUrl

        result, err = dishesSpider.scrape_dishes(googleMapUrl)
        if err:
            return pb2.CrawlDishesFromGoogleMapReply(success=False,
                                                     message=str(err),
                                                     dish=[])

        resultList = []
        for dish in result:
            d = pb2.Dish(name=dish.name,
                         description=dish.description,
                         image=dish.image,
                         price=dish.price,
                         category=dish.category)
            resultList.append(d)
        return pb2.CrawlDishesFromGoogleMapReply(success=True,
                                                 message="success",
                                                 dish=resultList)


def run():
    port = "5000"
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))

    pb2_grpc.add_SpiderServicer_to_server(Spider(), grpc_server)
    grpc_server.add_insecure_port('[::]:' + port)
    grpc_server.start()
    print("Server started, listening on " + port)
    grpc_server.wait_for_termination()


run()