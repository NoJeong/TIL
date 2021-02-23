## randint(low=0, high, size) (low~high값 반환)

>>> torch.randint(3, 5, (3,))
tensor([4, 3, 4])


>>> torch.randint(10, (2, 2))
tensor([[0, 2],
        [5, 5]])


>>> torch.randint(3, 10, (2, 2))
tensor([[4, 5],
        [6, 7]])


##rand(size) ( 0~1 의값 랜덤 반환)

>>> torch.rand(4)
tensor([ 0.5204,  0.2503,  0.3525,  0.5673])
>>> torch.rand(2, 3)
tensor([[ 0.8237,  0.5781,  0.6879],
        [ 0.3816,  0.7249,  0.0998]])