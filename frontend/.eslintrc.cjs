module.exports = {
  root: true,
  env: {
    browser: true,
    es2022: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
  },
  plugins: ['@typescript-eslint'],
  rules: {
    // Disallow plain .css imports - enforce SCSS-only styling
    'no-restricted-imports': [
      'error',
      {
        patterns: [
          {
            group: ['*.css'],
            message: 'Plain CSS imports are not allowed. Use SCSS (.scss) files instead.',
          },
        ],
      },
    ],
    // TypeScript-specific rules
    '@typescript-eslint/no-explicit-any': 'warn',
    'no-unused-vars': 'off',
    '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
  ignorePatterns: ['dist/', 'node_modules/', 'coverage/', '*.config.js', '*.config.cjs'],
}
