const sumar = require('./index');

test('debería devolver 4 al sumar 2 + 2', () => {
  expect(sumar(2, 2)).toBe(4);
});