# Micro Services

## gRPC

Présentation de l'architecture

![](https://grpc.io/img/landing-2.svg)

### Exercice 1 - Hello gRPC

D'après la [documentation officielle](https://grpc.io/docs/languages/python/quickstart/).

1. Initialiser le projet python [grpc_hello](./grpc_hello) avec uv

```bash
uv init --bare .
```

2. Ajouter les modules `grpcio` et `grpcio-tools`

```bash
uv add grpcio grpcio-tools
```

3. Créer le fichier `hello.proto`

```proto
syntax = "proto3";

service Greeter {
    rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}

```

4. Compiler le fichier `hello.proto` uniquement en Python : stub et server en Python

```bash
uv run python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. hello.proto
```

5. Créer un script python qui va implémenter le serveur
6. Créer un script python qui va faire office de client