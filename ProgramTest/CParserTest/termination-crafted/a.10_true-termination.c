

int test_fun(int x, int y)
{
    int c = 0;
    while (!(x == y)) {
        if (x > y) {
            y = y + 1;
        } else {
            x = x + 1;
        }
        c = c + 1;
    }
    return c;
}

int main() {
    return test_fun(0, 0);
}
