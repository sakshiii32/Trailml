# Language Translation Application

A web-based language translation application with a FastAPI backend and HTML/JavaScript frontend.

## Deployment Instructions

### Deploying to Vercel

1. Create a Vercel account at https://vercel.com
2. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```
3. Login to Vercel:
   ```bash
   vercel login
   ```
4. Deploy your application:
   ```bash
   vercel
   ```

The deployment will automatically:
- Deploy the FastAPI backend using Python runtime
- Serve the static frontend files
- Set up automatic deployments on push to main branch

## Environment Variables

Make sure to set these in your Vercel dashboard:
- Any environment variables your application needs

## API Endpoint

After deployment, update the API endpoint in `l.html` to match your Vercel deployment URL:
```javascript
axios.get('your-vercel-url/translate', {
```

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI
- Translation: Google Translate API
- Deployment: Vercel (Backend and Frontend)
