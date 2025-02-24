import { test, expect } from "vitest";
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/FARM/i);
  expect(linkElement).toBeInTheDocument();
});

test('dummy test always true', () => {
  expect(true).toBe(true);
});