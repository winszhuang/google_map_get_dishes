// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.2
// source: protos/crawl.proto

package pb

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// SpiderClient is the client API for Spider service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SpiderClient interface {
	CrawlDishesFromGoogleMap(ctx context.Context, in *CrawlDishesFromGoogleMapRequest, opts ...grpc.CallOption) (*CrawlDishesFromGoogleMapReply, error)
}

type spiderClient struct {
	cc grpc.ClientConnInterface
}

func NewSpiderClient(cc grpc.ClientConnInterface) SpiderClient {
	return &spiderClient{cc}
}

func (c *spiderClient) CrawlDishesFromGoogleMap(ctx context.Context, in *CrawlDishesFromGoogleMapRequest, opts ...grpc.CallOption) (*CrawlDishesFromGoogleMapReply, error) {
	out := new(CrawlDishesFromGoogleMapReply)
	err := c.cc.Invoke(ctx, "/crawl.Spider/CrawlDishesFromGoogleMap", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SpiderServer is the server API for Spider service.
// All implementations must embed UnimplementedSpiderServer
// for forward compatibility
type SpiderServer interface {
	CrawlDishesFromGoogleMap(context.Context, *CrawlDishesFromGoogleMapRequest) (*CrawlDishesFromGoogleMapReply, error)
	mustEmbedUnimplementedSpiderServer()
}

// UnimplementedSpiderServer must be embedded to have forward compatible implementations.
type UnimplementedSpiderServer struct {
}

func (UnimplementedSpiderServer) CrawlDishesFromGoogleMap(context.Context, *CrawlDishesFromGoogleMapRequest) (*CrawlDishesFromGoogleMapReply, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CrawlDishesFromGoogleMap not implemented")
}
func (UnimplementedSpiderServer) mustEmbedUnimplementedSpiderServer() {}

// UnsafeSpiderServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SpiderServer will
// result in compilation errors.
type UnsafeSpiderServer interface {
	mustEmbedUnimplementedSpiderServer()
}

func RegisterSpiderServer(s grpc.ServiceRegistrar, srv SpiderServer) {
	s.RegisterService(&Spider_ServiceDesc, srv)
}

func _Spider_CrawlDishesFromGoogleMap_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CrawlDishesFromGoogleMapRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SpiderServer).CrawlDishesFromGoogleMap(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/crawl.Spider/CrawlDishesFromGoogleMap",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SpiderServer).CrawlDishesFromGoogleMap(ctx, req.(*CrawlDishesFromGoogleMapRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Spider_ServiceDesc is the grpc.ServiceDesc for Spider service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Spider_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "crawl.Spider",
	HandlerType: (*SpiderServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CrawlDishesFromGoogleMap",
			Handler:    _Spider_CrawlDishesFromGoogleMap_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "protos/crawl.proto",
}
