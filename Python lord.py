<Project DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003" ToolsVersion="4.0">
  <PropertyGroup>
    <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>
    <SchemaVersion>2.0</SchemaVersion>
    <ProjectGuid>0f55b376-0175-4cff-ba71-fbff3a2447d2</ProjectGuid>
    <ProjectHome>.</ProjectHome>
    <StartupFile>Python_lord.py</StartupFile>
    <SearchPath>
    </SearchPath>
    <WorkingDirectory>.</WorkingDirectory>
    <OutputPath>.</OutputPath>
    <Name>Python lord</Name>
    <RootNamespace>Python lord</RootNamespace>
    <InterpreterId>MSBuild|env2|$(MSBuildProjectFullPath)</InterpreterId>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)' == 'Debug' ">
    <DebugSymbols>true</DebugSymbols>
    <EnableUnmanagedDebugging>false</EnableUnmanagedDebugging>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)' == 'Release' ">
    <DebugSymbols>true</DebugSymbols>
    <EnableUnmanagedDebugging>false</EnableUnmanagedDebugging>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="Python_lord.py" />
  </ItemGroup>
  <ItemGroup>
    <InterpreterReference Include="Global|PythonCore|3.9" />
  </ItemGroup>
  <ItemGroup>
    <Interpreter Include=".vs\Python lord\FileContentIndex\env2\">
      <Id>env2</Id>
      <Version>3.9</Version>
      <Description>env2 (Python 3.9 (64-bit))</Description>
      <InterpreterPath>Scripts\python.exe</InterpreterPath>
      <WindowsInterpreterPath>Scripts\pythonw.exe</WindowsInterpreterPath>
      <PathEnvironmentVariable>PYTHONPATH</PathEnvironmentVariable>
      <Architecture>X64</Architecture>
    </Interpreter>
    <Interpreter Include="env1\">
      <Id>env1</Id>
      <Version>3.9</Version>
      <Description>env1 (Python 3.9 (64-bit))</Description>
      <InterpreterPath>Scripts\python.exe</InterpreterPath>
      <WindowsInterpreterPath>Scripts\pythonw.exe</WindowsInterpreterPath>
      <PathEnvironmentVariable>PYTHONPATH</PathEnvironmentVariable>
      <Architecture>X64</Architecture>
    </Interpreter>
    <Interpreter Include="env\">
      <Id>env</Id>
      <Version>3.9</Version>
      <Description>env (Python 3.9 (64-bit))</Description>
      <InterpreterPath>Scripts\python.exe</InterpreterPath>
      <WindowsInterpreterPath>Scripts\pythonw.exe</WindowsInterpreterPath>
      <PathEnvironmentVariable>PYTHONPATH</PathEnvironmentVariable>
      <Architecture>X64</Architecture>
    </Interpreter>
  </ItemGroup>
  <Import Project="$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\Python Tools\Microsoft.PythonTools.targets" />
  <!-- Uncomment the CoreCompile target to enable the Build command in
       Visual Studio and specify your pre- and post-build commands in
       the BeforeBuild and AfterBuild targets below. -->
  <!--<Target Name="CoreCompile" />-->
  <Target Name="BeforeBuild">
  </Target>
  <Target Name="AfterBuild">
  </Target>
</Project>
