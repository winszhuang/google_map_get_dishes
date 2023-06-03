package main

import (
	"context"
	"log"
	"time"

	"go/pb"

	"google.golang.org/grpc"
)

const (
	address     = "localhost:5000"
	defaultName = "world"
)

func main() {
	conn, err := grpc.Dial(":5000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	c := pb.NewSpiderClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second*10)
	defer cancel()

	r, err := c.CrawlDishesFromGoogleMap(
		ctx,
		&pb.CrawlDishesFromGoogleMapRequest{GoogleMapUrl: "https://www.google.com.tw/maps/place/%E7%89%A7%E7%A6%BE%E5%A0%82%E5%8F%B0%E4%B8%AD%E5%8C%97%E5%B9%B3%E5%BA%97/@24.1714575,120.6749791,18.75z/data=!4m6!3m5!1s0x346917901f6b4a5b:0xf507d5c683b79253!8m2!3d24.1713975!4d120.6756103!16s%2Fg%2F11rr2kb7kx?entry=ttu"},
	)
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}

	log.Println(r.Success)
	log.Println(r.Message)
	if r.Success {
		for _, dish := range r.Dish {
			log.Println("-------")
			log.Println(dish.Name)
			log.Println(dish.Description)
		}
	}
}
