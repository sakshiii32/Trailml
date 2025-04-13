# Deployment Guide: Connecting Vercel Backend to GitHub Pages Frontend

This guide will walk you through deploying your language translation application with the frontend on GitHub Pages and the backend on Vercel.

## Prerequisites

- A GitHub account
- A Vercel account (free to create at [vercel.com](https://vercel.com))
- Your code pushed to a GitHub repository

## Step 1: Deploy Backend to Vercel

1. **Create a Vercel account** (if you don't have one already)
   - Go to [vercel.com](https://vercel.com) and sign up using your GitHub account for seamless integration

2. **Install Vercel CLI** (optional, you can also deploy directly from the Vercel dashboard)
   ```
   npm install -g vercel
   ```

3. **Deploy to Vercel using the Dashboard (Recommended Method)**
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Vercel will automatically detect your project settings from `vercel.json`
   - Click "Deploy"
   - Once deployed, Vercel will provide you with a deployment URL (e.g., `https://your-project.vercel.app`)
   - **Save this URL** as you'll need it for your frontend

4. **Alternative: Deploy using Vercel CLI**
   - Open a terminal in your project directory
   - Run `vercel login` and follow the prompts to log in
   - Run `vercel` and follow the prompts
   - When asked about the settings, use the defaults as they'll be read from your `vercel.json`

## Step 2: Update Frontend to Use Vercel Backend

Your `index.html` already has the conditional logic to use different backend URLs based on the environment:

```javascript
// Get the backend URL based on the environment
const backendUrl = window.location.hostname.includes('github.io')
    ? 'https://aiml-project.vercel.app/translate'
    : '/translate';
```

You need to update this URL to your actual Vercel deployment URL:

1. Open `index.html`
2. Find the code block above
3. Replace `'https://aiml-project.vercel.app/translate'` with your Vercel deployment URL + `/translate`
   - For example: `'https://your-project.vercel.app/translate'`
4. Save the file

## Step 3: Push Updated Frontend to GitHub

1. Commit your changes:
   ```
   git add index.html
   git commit -m "Update backend URL to Vercel deployment"
   git push
   ```

2. GitHub Actions will automatically deploy your updated frontend to GitHub Pages (based on your existing workflow files)

## Step 4: Verify the Connection

1. Wait a few minutes for GitHub Pages to update
2. Visit your GitHub Pages URL (typically `https://yourusername.github.io/repository-name/`)
3. Test the translation functionality
4. If it works, congratulations! Your frontend on GitHub Pages is now successfully connected to your backend on Vercel

## Troubleshooting

- **CORS Issues**: If you encounter CORS errors, verify that your Vercel backend has the proper CORS configuration (your `langbackend.py` already has this set up)
- **404 Errors**: Make sure the path to your API endpoint is correct in both the frontend and `vercel.json`
- **Deployment Failures**: Check the Vercel deployment logs for any errors

## Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [FastAPI on Vercel](https://vercel.com/guides/deploying-fastapi-with-vercel)