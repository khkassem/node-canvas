# dependency walker will help us figure out which DLLs 
# canvas.node directly and indirectly uses
wget --no-verbose --no-clobber http://www.dependencywalker.com/depends22_x64.zip
unzip -u depends22_x64.zip

# write recurisve dependencies of canvas.node into depends.csv
./depends -c -oc:depends.csv /c/devz/workspace/node-canvas-master/build/Release/canvas.node;

[ -f depends.csv ] || {
  echo "error invoking depends.exe";
  exit 1;
}

# case-insensitive intersection of 2nd column of depends.csv
# and all files ending in .dll in the mingw64 directory
copies=$(comm -12 \
  <(cat depends.csv | cut -d ',' -f2 | sed 's/"//g' | tr '[:upper:]' '[:lower:]' | sort) \
  <(find /mingw32/bin -name '*.dll' -printf "%f\n" | tr '[:upper:]' '[:lower:]' | sort) \
);

echo $copies

for dll in $copies; do
  cp /mingw32/bin/$dll /c/devz/workspace/node-canvas-master/build/Release
	
  #copie all dependencies of this dll
  ./depends -c -oc:$dll-depends.csv /mingw32/bin/$dll;
  
   # case-insensitive intersection of 2nd column of depends.csv
   # and all files ending in .dll in the mingw64 directory
	copies2=$(comm -12 \
	  <(cat $dll-depends.csv | cut -d ',' -f2 | sed 's/"//g' | tr '[:upper:]' '[:lower:]' | sort) \
	  <(find /mingw32/bin -name '*.dll' -printf "%f\n" | tr '[:upper:]' '[:lower:]' | sort) \
	);
	
	for dll2 in $copies2; do
	  cp /mingw32/bin/$dll2 /c/devz/workspace/node-canvas-master/build/Release
	done;
done;
