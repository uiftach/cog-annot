# GitHub Setup Guide for Cog-Annot

## Step 1: Install Git

1. Download Git for Windows: https://git-scm.com/download/win
2. Run the installer (accept default settings)
3. Restart your terminal/PowerShell after installation

## Step 2: Create GitHub Account (if needed)

1. Go to https://github.com
2. Sign up for a free account
3. Verify your email address

## Step 3: Create New Repository on GitHub

1. Log in to GitHub
2. Click the **+** icon (top right) → **New repository**
3. Repository name: `cog-annot`
4. Description: "Object-centered semantic annotation system for descriptive texts"
5. Choose: **Public** (so others can access) or **Private**
6. **DO NOT** check "Initialize with README" (we already have one)
7. Click **Create repository**

## Step 4: Initialize Local Git Repository

Open PowerShell in your project folder and run:

```powershell
cd c:\Users\USER\uri\projects\cog-annot

# Initialize git
git init

# Configure your identity (use your GitHub email/name)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Cog-Annot annotation system with Aristotle HA example"
```

## Step 5: Connect to GitHub and Push

Replace `[your-username]` with your actual GitHub username:

```powershell
# Add remote repository
git remote add origin https://github.com/[your-username]/cog-annot.git

# Rename branch to main (GitHub default)
git branch -M main

# Push to GitHub
git push -u origin main
```

You may be prompted to authenticate - use your GitHub credentials.

## Step 6: Share with Others

Once pushed, share this URL with collaborators:
```
https://github.com/[your-username]/cog-annot
```

## For Collaborators to Contribute

### Option A: Clone and Contribute (Requires permissions)

```powershell
# Clone the repository
git clone https://github.com/[username]/cog-annot.git
cd cog-annot

# Create a new folder for their work
mkdir "MyCorpus"
cd MyCorpus

# Add annotated texts
# ... create files ...

# Commit and push
git add .
git commit -m "Add MyCorpus annotations"
git push
```

### Option B: Fork and Pull Request (Public contribution)

1. Collaborator clicks **Fork** on your GitHub repository
2. They clone their fork
3. Make changes and commit
4. Submit a **Pull Request** back to your repository
5. You review and merge their contributions

## Updating Your Local Repository

```powershell
# Get latest changes from GitHub
git pull

# See what changed
git log --oneline
```

## Quick Reference

```powershell
# Check status
git status

# Add new/modified files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push

# Pull latest changes
git pull
```

## Troubleshooting

### "git is not recognized"
- Restart PowerShell after installing Git
- Or add Git to PATH: `C:\Program Files\Git\cmd`

### Authentication issues
- Use GitHub Personal Access Token instead of password
- Generate at: Settings → Developer settings → Personal access tokens

### Merge conflicts
```powershell
# See conflicted files
git status

# Edit files to resolve conflicts
# Then:
git add [resolved-file]
git commit -m "Resolve merge conflict"
git push
```

## Best Practices

1. **Commit often** with descriptive messages
2. **Pull before push** to avoid conflicts
3. **Use branches** for experimental work:
   ```powershell
   git checkout -b my-new-feature
   # ... make changes ...
   git push -u origin my-new-feature
   ```
4. **Write clear commit messages**: "Add Plato corpus annotations" not just "updates"

## Repository Structure Recommendations

```
cog-annot/
├── README.md
├── INSTRUCTIONS.md
├── .gitignore
├── Aristoteles/
│   └── HA/
├── [Author1]/
│   ├── [Text1].txt
│   └── [Text2].txt
├── [Author2]/
│   └── [Corpus]/
└── [Collaborator1]/
    └── [TheirTexts]/
```

Each collaborator can have their own folder(s) for their annotated texts.
