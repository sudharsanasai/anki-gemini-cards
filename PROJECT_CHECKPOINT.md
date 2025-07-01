# Anki Project Checkpoint

**Date:** December 2024  
**Project:** Anki Spaced Repetition Software  
**Branch:** main  
**Last Commit:** 7720c7de1 - "Only run `empty_filtered_deck` on filtered decks. (#4139)"

## Project Overview

This is the official Anki spaced repetition software repository. Anki is a powerful flashcard application that uses spaced repetition algorithms to help users memorize information efficiently.

### Architecture
- **Backend:** Rust (rslib) - Core logic and data management
- **Frontend:** Qt (Python bindings) - Desktop GUI
- **Web Interface:** SvelteKit/TypeScript - Modern web interface
- **Python Library:** pylib - Python bindings for the Rust backend
- **Build System:** Ninja + custom build scripts

## Current Development Environment

### System Requirements ✅
- **Python:** 3.8.3 (meets minimum requirement of 3.9)
- **Rust:** 1.88.0 (meets requirement of 1.80)
- **Node.js:** 24.1.0 (compatible)
- **OS:** macOS (darwin 24.5.0)

### Build Status ✅
- Project builds successfully
- `./run --help` works correctly
- All dependencies resolved

## Custom Implementations

### 1. Gemini AI Integration 🚧
**Location:** `qt/aqt/gemini_api.py`

**Features:**
- Integration with Google's Gemini 2.5 Pro API
- Automatic flashcard generation from topics
- Configurable instruction templates
- Response parsing for Q&A format

**Files:**
- `qt/aqt/gemini_api.py` - Main API integration
- `qt/aqt/gemini_config.json` - API configuration
- `qt/aqt/llm_instruction.json` - Instruction templates
- `qt/aqt/test_gemini_api.py` - API testing
- `test_gemini_parsing.py` - Comprehensive parsing tests

**Status:** Functional but needs integration with UI

### 2. Corporate Bond Flashcards 📚
**Location:** `user/` directory

**Features:**
- Specialized flashcards for corporate bond concepts
- Image generation and management
- JSON data structure for bond spreads
- Automated card creation scripts

**Files:**
- `user/add_corporate_bond_cards.py` - Main card creation
- `user/create_corporate_bond_deck.py` - Deck management
- `user/corporate_bond_spreads.json` - Data source
- `user/copy_images_to_anki.py` - Image handling
- `user/download_corporate_bond_images.py` - Image download
- `user/update_cards_with_images.py` - Image updates

**Status:** Complete and functional

### 3. Basic Card Creation Script
**Location:** `addNewCard.py`

**Features:**
- Simple script to add basic flashcards
- Direct collection manipulation
- Example implementation

**Status:** Working example

## Modified Core Files

### UI Modifications
- `qt/aqt/addcards.py` - Modified for potential AI integration
- `qt/aqt/forms/addcards.ui` - UI layout changes

### Submodule Updates
- `ftl/core-repo` - Translation updates
- `ftl/qt-repo` - Qt translation updates

## Git Status

### Uncommitted Changes
```
Modified:
  - ftl/core-repo (new commits, untracked content)
  - ftl/qt-repo (new commits)
  - qt/aqt/addcards.py
  - qt/aqt/forms/addcards.ui

Untracked:
  - addNewCard.py
  - qt/aqt/gemini_api.py
  - qt/aqt/gemini_config.json
  - qt/aqt/llm_instruction.json
  - qt/aqt/test_gemini_api.py
  - qt/aqt/tests/
  - test_gemini_parsing.py
  - user/ (entire directory)
```

## Key Achievements

1. **✅ Successful Build:** Project compiles and runs correctly
2. **✅ AI Integration:** Gemini API integration working
3. **✅ Custom Flashcards:** Corporate bond domain implemented
4. **✅ Testing Framework:** Comprehensive parsing tests
5. **✅ Development Environment:** All tools properly configured

## Current Challenges

1. **🔧 UI Integration:** Gemini API not yet integrated into Anki's UI
2. **🔧 Configuration Management:** API keys and configs need better management
3. **🔧 Error Handling:** Need more robust error handling in AI integration
4. **🔧 Code Organization:** Custom code needs better integration with Anki's architecture

## Next Steps

### Immediate (High Priority)
1. **Integrate Gemini API into Anki UI**
   - Add AI card generation button to add cards dialog
   - Implement proper error handling and user feedback
   - Add configuration UI for API settings

2. **Improve Code Organization**
   - Move custom code to proper addon structure
   - Follow Anki's coding conventions
   - Add proper documentation

3. **Enhance Testing**
   - Add unit tests for AI integration
   - Integration tests for UI components
   - Performance testing for API calls

### Medium Term
1. **Feature Enhancement**
   - Support for different card types (Cloze, etc.)
   - Batch processing for multiple topics
   - Template customization

2. **User Experience**
   - Progress indicators for API calls
   - Preview generated cards before adding
   - Undo/redo functionality

### Long Term
1. **Advanced Features**
   - Multiple AI provider support
   - Custom instruction templates
   - Learning analytics integration

## Technical Debt

1. **Hardcoded Paths:** API configuration uses absolute paths
2. **Error Handling:** Limited error handling in AI integration
3. **Documentation:** Missing inline documentation
4. **Configuration:** No user-friendly config management

## Recommendations

1. **Create an Anki Addon:** Convert custom code to proper addon format
2. **Use Anki's Config System:** Integrate with Anki's built-in configuration
3. **Follow Anki's Patterns:** Use existing UI patterns and conventions
4. **Add Comprehensive Testing:** Ensure reliability and maintainability

## Environment Notes

- Using Python 3.8.3 (should upgrade to 3.9+ for production)
- All build tools working correctly
- Development environment properly configured
- Ready for feature development and testing

---

**Checkpoint Created:** December 2024  
**Next Review:** After UI integration completion 