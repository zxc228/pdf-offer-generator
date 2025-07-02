FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
COPY tsconfig.json ./
COPY next.config.ts ./
COPY postcss.config.mjs ./
COPY eslint.config.mjs ./
COPY public ./public
COPY src ./src

RUN npm install --frozen-lockfile
RUN npm run build

FROM node:20-alpine
WORKDIR /app

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/next.config.ts ./
COPY --from=builder /app/postcss.config.mjs ./
COPY --from=builder /app/eslint.config.mjs ./
COPY --from=builder /app/src ./src

RUN npm ci --omit=dev

ENV NODE_ENV=production
EXPOSE 3000

CMD ["npm", "start"]
