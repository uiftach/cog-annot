# Collaboration & Quality Control Guide

## Setup: Branch Protection (Do This First)

1. Go to: https://github.com/uiftach/cog-annot/settings/branches
2. Click **"Add branch protection rule"**
3. Branch name pattern: `main`
4. Check these options:
   - ✅ **Require a pull request before merging**
   - ✅ **Require approvals** (1 approval minimum)
   - ✅ **Dismiss stale pull request approvals when new commits are pushed**
5. Click **"Create"**

Now collaborators **cannot push directly** to main - they must submit Pull Requests.

## For Collaborators: How to Contribute

### Option A: Fork Method (Recommended for external contributors)

```bash
# 1. Fork the repository on GitHub (click "Fork" button)

# 2. Clone YOUR fork
git clone https://github.com/[their-username]/cog-annot.git
cd cog-annot

# 3. Create a folder and add files
mkdir "MyCorpus"
# ... add annotated files ...

# 4. Commit and push to their fork
git add .
git commit -m "Add MyCorpus annotations"
git push

# 5. On GitHub, click "Contribute" → "Open pull request"
```

### Option B: Branch Method (For added collaborators)

```bash
# 1. Clone the repository
git clone https://github.com/uiftach/cog-annot.git
cd cog-annot

# 2. Create a new branch
git checkout -b add-mycorpus

# 3. Add your work
mkdir "MyCorpus"
# ... add files ...

# 4. Commit and push branch
git add .
git commit -m "Add MyCorpus annotations"
git push -u origin add-mycorpus

# 5. On GitHub, create Pull Request from your branch
```

## For You: Reviewing Pull Requests

### 1. When someone submits a Pull Request:

- Go to: https://github.com/uiftach/cog-annot/pulls
- Click on the Pull Request
- Review the **"Files changed"** tab to see exactly what they added/modified

### 2. Review checklist:

- ✅ Did they follow the annotation format? `⟨CogType#track: text⟩`
- ✅ Did they create their own folder (not modify yours)?
- ✅ Do annotations follow INSTRUCTIONS.md?
- ✅ Are track numbers consistent?
- ✅ Is the work complete?

### 3. Actions you can take:

**Approve and merge:**
```
Click "Review changes" → "Approve" → "Merge pull request"
```

**Request changes:**
```
Click "Review changes" → "Request changes" → Add comments
```

**Add inline comments:**
```
Click on any line in "Files changed" → Add comment
```

### 4. Pull the merged changes locally:

```powershell
git pull origin main
```

## Monitor Activity

### View all contributors:
```powershell
git log --pretty=format:"%an <%ae>" | sort | uniq
```

### See what a specific person did:
```powershell
git log --author="name@email.com" --oneline
```

### See changes in a specific folder:
```powershell
git log --follow -- "FolderName/*"
```

### View detailed changes:
```powershell
# See what changed in last commit
git show

# See changes in specific file
git log -p -- "path/to/file.txt"
```

## Quality Control

### Before approving a Pull Request:

1. **Check file structure:**
   ```powershell
   # View the folder they added
   git diff main origin/[branch-name] --name-status
   ```

2. **Review specific file:**
   ```powershell
   # See the diff for a specific file
   git diff main origin/[branch-name] -- "path/to/file.txt"
   ```

3. **Test locally before merging:**
   ```powershell
   # Fetch their branch
   git fetch origin [branch-name]
   
   # Check it out locally
   git checkout [branch-name]
   
   # Review files
   # ... if good, merge via GitHub
   
   # Return to main
   git checkout main
   ```

### If you need to reject changes:

In the Pull Request on GitHub:
1. Click **"Close pull request"** (without merging)
2. Add explanation in comments
3. They can revise and resubmit

## Rollback if Needed

If something wrong gets merged:

```powershell
# See recent commits
git log --oneline -10

# Revert a specific commit (creates new commit undoing it)
git revert [commit-hash]
git push

# Or reset to previous state (careful - rewrites history)
git reset --hard [good-commit-hash]
git push --force
```

## Adding Collaborators

If you want to give someone direct access:

1. Go to: https://github.com/uiftach/cog-annot/settings/access
2. Click **"Add people"**
3. Enter their GitHub username
4. Choose permission level:
   - **Read**: Can only view and fork
   - **Triage**: Can manage issues (if you add issue tracking)
   - **Write**: Can push branches (but still need PR for main if protected)

**Recommendation**: Start with **Read** access only, let them submit Pull Requests.

## Summary Workflow

1. ✅ **You**: Enable branch protection on `main`
2. 📝 **Collaborator**: Creates fork/branch, adds their work
3. 📤 **Collaborator**: Submits Pull Request
4. 👀 **You**: Review changes on GitHub
5. ✅ **You**: Approve and merge (or request changes)
6. 📥 **You**: Pull merged changes locally with `git pull`

This gives you complete control while making it easy for others to contribute.
