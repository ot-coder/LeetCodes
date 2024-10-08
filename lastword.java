class lastword {
    public int lengthOfLastWord(String s) {
    s = s.trim();

        if (s.length() == 0) {
            return 0;
        }

        int LastSpaceIndex = s.lastIndexOf(" ");
        /*String[] characters = s.split("");
        int index = -1;

        for (int i = characters.length - 1; i >=0; i--){
            if (characters[i].equals (" ")) {
                index = i + 1;
                break;
            }
        }
        
        return characters.length - index; */
        return s.length() - LastSpaceIndex - 1;
    }
}