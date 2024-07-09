def generate_sequence(n: int) -> str | int | list[int]:
    """
    Generate a sequence of integers
    where each num appears num times (e.g. 122333444455555...)
    and the sequence length equals n.

    """
    if n <= 0:
        return ''
    if n == 1:
        return 1
    result = []
    result_len = 0
    num = 1
    while result_len < n:
        diff = n - result_len
        num_count = min(diff, num)
        result += [num] * num_count
        result_len += num_count
        num += 1

    return result


if __name__ == '__main__':
    print(*generate_sequence(n=50), sep='')

    for n in range(0, 100, 5):
        result = generate_sequence(n=n)
        assert len(result) == n, 'Длина последовательности не соответствует значению n'
