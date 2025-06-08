# SNMP MIB module (RUIJIE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(ruijieApMacAddr,) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApMacAddr")

(ruijieMemoryPoolCurrentUtilization,
 ruijieNodeMemoryPoolCurrentUtilization,
 ruijieNodeMemoryPoolName) = mibBuilder.importSymbols(
    "RUIJIE-MEMORY-MIB",
    "ruijieMemoryPoolCurrentUtilization",
    "ruijieNodeMemoryPoolCurrentUtilization",
    "ruijieNodeMemoryPoolName")

(Percent,
 ruijieCPUUtilization1Min,
 ruijieNodeCPUTotal1min,
 ruijieNodeCPUTotalName) = mibBuilder.importSymbols(
    "RUIJIE-PROCESS-MIB",
    "Percent",
    "ruijieCPUUtilization1Min",
    "ruijieNodeCPUTotal1min",
    "ruijieNodeCPUTotalName")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieSystemMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSystemMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSystemMIBObjects = _RuijieSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1)
)


class _RuijieSystemHwVersion_Type(DisplayString):
    """Custom type ruijieSystemHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSystemHwVersion_Type.__name__ = "DisplayString"
_RuijieSystemHwVersion_Object = MibScalar
ruijieSystemHwVersion = _RuijieSystemHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 1),
    _RuijieSystemHwVersion_Type()
)
ruijieSystemHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemHwVersion.setStatus("current")


class _RuijieSystemSwVersion_Type(DisplayString):
    """Custom type ruijieSystemSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSystemSwVersion_Type.__name__ = "DisplayString"
_RuijieSystemSwVersion_Object = MibScalar
ruijieSystemSwVersion = _RuijieSystemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 2),
    _RuijieSystemSwVersion_Type()
)
ruijieSystemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSwVersion.setStatus("current")


class _RuijieSystemBootVersion_Type(DisplayString):
    """Custom type ruijieSystemBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSystemBootVersion_Type.__name__ = "DisplayString"
_RuijieSystemBootVersion_Object = MibScalar
ruijieSystemBootVersion = _RuijieSystemBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 3),
    _RuijieSystemBootVersion_Type()
)
ruijieSystemBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemBootVersion.setStatus("current")


class _RuijieSystemSysCtrlVersion_Type(DisplayString):
    """Custom type ruijieSystemSysCtrlVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSystemSysCtrlVersion_Type.__name__ = "DisplayString"
_RuijieSystemSysCtrlVersion_Object = MibScalar
ruijieSystemSysCtrlVersion = _RuijieSystemSysCtrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 4),
    _RuijieSystemSysCtrlVersion_Type()
)
ruijieSystemSysCtrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSysCtrlVersion.setStatus("current")
_RuijieSystemParametersSave_Type = Integer32
_RuijieSystemParametersSave_Object = MibScalar
ruijieSystemParametersSave = _RuijieSystemParametersSave_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 5),
    _RuijieSystemParametersSave_Type()
)
ruijieSystemParametersSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemParametersSave.setStatus("current")


class _RuijieSystemOutBandRate_Type(Integer32):
    """Custom type ruijieSystemOutBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 1),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud115200", 5))
    )


_RuijieSystemOutBandRate_Type.__name__ = "Integer32"
_RuijieSystemOutBandRate_Object = MibScalar
ruijieSystemOutBandRate = _RuijieSystemOutBandRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 6),
    _RuijieSystemOutBandRate_Type()
)
ruijieSystemOutBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemOutBandRate.setStatus("current")


class _RuijieSystemReset_Type(Integer32):
    """Custom type ruijieSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("restart", 1))
    )


_RuijieSystemReset_Type.__name__ = "Integer32"
_RuijieSystemReset_Object = MibScalar
ruijieSystemReset = _RuijieSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 7),
    _RuijieSystemReset_Type()
)
ruijieSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemReset.setStatus("current")


class _RuijieSwitchLayer_Type(Integer32):
    """Custom type ruijieSwitchLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2),
          ("router", 3))
    )


_RuijieSwitchLayer_Type.__name__ = "Integer32"
_RuijieSwitchLayer_Object = MibScalar
ruijieSwitchLayer = _RuijieSwitchLayer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 8),
    _RuijieSwitchLayer_Type()
)
ruijieSwitchLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSwitchLayer.setStatus("current")


class _RuijieSystemHwPower_Type(Integer32):
    """Custom type ruijieSystemHwPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rpsNoLink", 1),
          ("rpsLinkAndNoPower", 2),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsLinkAndPower", 4))
    )


_RuijieSystemHwPower_Type.__name__ = "Integer32"
_RuijieSystemHwPower_Object = MibScalar
ruijieSystemHwPower = _RuijieSystemHwPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 9),
    _RuijieSystemHwPower_Type()
)
ruijieSystemHwPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemHwPower.setStatus("current")


class _RuijieSystemHwFan_Type(Integer32):
    """Custom type ruijieSystemHwFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("work", 1),
          ("stop", 2))
    )


_RuijieSystemHwFan_Type.__name__ = "Integer32"
_RuijieSystemHwFan_Object = MibScalar
ruijieSystemHwFan = _RuijieSystemHwFan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 10),
    _RuijieSystemHwFan_Type()
)
ruijieSystemHwFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemHwFan.setStatus("current")


class _RuijieSystemOutBandTimeout_Type(Integer32):
    """Custom type ruijieSystemOutBandTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuijieSystemOutBandTimeout_Type.__name__ = "Integer32"
_RuijieSystemOutBandTimeout_Object = MibScalar
ruijieSystemOutBandTimeout = _RuijieSystemOutBandTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 11),
    _RuijieSystemOutBandTimeout_Type()
)
ruijieSystemOutBandTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemOutBandTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    ruijieSystemOutBandTimeout.setUnits("seconds")


class _RuijieSystemTelnetTimeout_Type(Integer32):
    """Custom type ruijieSystemTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuijieSystemTelnetTimeout_Type.__name__ = "Integer32"
_RuijieSystemTelnetTimeout_Object = MibScalar
ruijieSystemTelnetTimeout = _RuijieSystemTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 12),
    _RuijieSystemTelnetTimeout_Type()
)
ruijieSystemTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemTelnetTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    ruijieSystemTelnetTimeout.setUnits("seconds")


class _RuijieSystemMainFile_Type(DisplayString):
    """Custom type ruijieSystemMainFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieSystemMainFile_Type.__name__ = "DisplayString"
_RuijieSystemMainFile_Object = MibScalar
ruijieSystemMainFile = _RuijieSystemMainFile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 13),
    _RuijieSystemMainFile_Type()
)
ruijieSystemMainFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMainFile.setStatus("current")
_RuijieSystemCurrentPower_Type = Integer32
_RuijieSystemCurrentPower_Object = MibScalar
ruijieSystemCurrentPower = _RuijieSystemCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 14),
    _RuijieSystemCurrentPower_Type()
)
ruijieSystemCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemCurrentPower.setStatus("current")
_RuijieSystemRemainPower_Type = Integer32
_RuijieSystemRemainPower_Object = MibScalar
ruijieSystemRemainPower = _RuijieSystemRemainPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 15),
    _RuijieSystemRemainPower_Type()
)
ruijieSystemRemainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemRemainPower.setStatus("current")
_RuijieSystemTemperature_Type = Integer32
_RuijieSystemTemperature_Object = MibScalar
ruijieSystemTemperature = _RuijieSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 16),
    _RuijieSystemTemperature_Type()
)
ruijieSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemTemperature.setStatus("current")
_RuijieSystemElectricalSourceNum_Type = Integer32
_RuijieSystemElectricalSourceNum_Object = MibScalar
ruijieSystemElectricalSourceNum = _RuijieSystemElectricalSourceNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 17),
    _RuijieSystemElectricalSourceNum_Type()
)
ruijieSystemElectricalSourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalSourceNum.setStatus("current")
_RuijieSystemElectricalSourceIsNormalTable_Object = MibTable
ruijieSystemElectricalSourceIsNormalTable = _RuijieSystemElectricalSourceIsNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    ruijieSystemElectricalSourceIsNormalTable.setStatus("current")
_RuijieSystemElectricalSourceIsNormalEntry_Object = MibTableRow
ruijieSystemElectricalSourceIsNormalEntry = _RuijieSystemElectricalSourceIsNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 18, 1)
)
ruijieSystemElectricalSourceIsNormalEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemElectricalSourceIsNormalIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemElectricalSourceIsNormalEntry.setStatus("current")
_RuijieSystemElectricalSourceIsNormalIndex_Type = Integer32
_RuijieSystemElectricalSourceIsNormalIndex_Object = MibTableColumn
ruijieSystemElectricalSourceIsNormalIndex = _RuijieSystemElectricalSourceIsNormalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 18, 1, 1),
    _RuijieSystemElectricalSourceIsNormalIndex_Type()
)
ruijieSystemElectricalSourceIsNormalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalSourceIsNormalIndex.setStatus("current")


class _RuijieSystemElectricalSourceIsNormal_Type(Integer32):
    """Custom type ruijieSystemElectricalSourceIsNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6),
          ("linefail", 7))
    )


_RuijieSystemElectricalSourceIsNormal_Type.__name__ = "Integer32"
_RuijieSystemElectricalSourceIsNormal_Object = MibTableColumn
ruijieSystemElectricalSourceIsNormal = _RuijieSystemElectricalSourceIsNormal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 18, 1, 2),
    _RuijieSystemElectricalSourceIsNormal_Type()
)
ruijieSystemElectricalSourceIsNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalSourceIsNormal.setStatus("current")
_RuijieSystemElectricalSourceName_Type = DisplayString
_RuijieSystemElectricalSourceName_Object = MibTableColumn
ruijieSystemElectricalSourceName = _RuijieSystemElectricalSourceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 18, 1, 3),
    _RuijieSystemElectricalSourceName_Type()
)
ruijieSystemElectricalSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalSourceName.setStatus("current")
_RuijieSystemCurrentVoltage_Type = Integer32
_RuijieSystemCurrentVoltage_Object = MibScalar
ruijieSystemCurrentVoltage = _RuijieSystemCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 19),
    _RuijieSystemCurrentVoltage_Type()
)
ruijieSystemCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemCurrentVoltage.setStatus("current")
_RuijieSystemFanNUM_Type = Integer32
_RuijieSystemFanNUM_Object = MibScalar
ruijieSystemFanNUM = _RuijieSystemFanNUM_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 20),
    _RuijieSystemFanNUM_Type()
)
ruijieSystemFanNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanNUM.setStatus("current")
_RuijieSystemFanIsNormalTable_Object = MibTable
ruijieSystemFanIsNormalTable = _RuijieSystemFanIsNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    ruijieSystemFanIsNormalTable.setStatus("current")
_RuijieSystemFanIsNormalEntry_Object = MibTableRow
ruijieSystemFanIsNormalEntry = _RuijieSystemFanIsNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 21, 1)
)
ruijieSystemFanIsNormalEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanIsNormalIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanIsNormalEntry.setStatus("current")
_RuijieSystemFanIsNormalIndex_Type = Integer32
_RuijieSystemFanIsNormalIndex_Object = MibTableColumn
ruijieSystemFanIsNormalIndex = _RuijieSystemFanIsNormalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 21, 1, 1),
    _RuijieSystemFanIsNormalIndex_Type()
)
ruijieSystemFanIsNormalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanIsNormalIndex.setStatus("current")


class _RuijieSystemFanIsNormal_Type(Integer32):
    """Custom type ruijieSystemFanIsNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6),
          ("linefail", 7))
    )


_RuijieSystemFanIsNormal_Type.__name__ = "Integer32"
_RuijieSystemFanIsNormal_Object = MibTableColumn
ruijieSystemFanIsNormal = _RuijieSystemFanIsNormal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 21, 1, 2),
    _RuijieSystemFanIsNormal_Type()
)
ruijieSystemFanIsNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanIsNormal.setStatus("current")
_RuijieSystemFanName_Type = DisplayString
_RuijieSystemFanName_Object = MibTableColumn
ruijieSystemFanName = _RuijieSystemFanName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 21, 1, 3),
    _RuijieSystemFanName_Type()
)
ruijieSystemFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanName.setStatus("current")
_RuijieSystemFanSpeed_Type = Integer32
_RuijieSystemFanSpeed_Object = MibTableColumn
ruijieSystemFanSpeed = _RuijieSystemFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 21, 1, 4),
    _RuijieSystemFanSpeed_Type()
)
ruijieSystemFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanSpeed.setStatus("current")
_RuijieSystemReloadTimeRemain_Type = Integer32
_RuijieSystemReloadTimeRemain_Object = MibScalar
ruijieSystemReloadTimeRemain = _RuijieSystemReloadTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 22),
    _RuijieSystemReloadTimeRemain_Type()
)
ruijieSystemReloadTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemReloadTimeRemain.setStatus("current")
_RuijieSystemTemperatureTable_Object = MibTable
ruijieSystemTemperatureTable = _RuijieSystemTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    ruijieSystemTemperatureTable.setStatus("current")
_RuijieSystemTemperatureEntry_Object = MibTableRow
ruijieSystemTemperatureEntry = _RuijieSystemTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23, 1)
)
ruijieSystemTemperatureEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemTemperatureIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemTemperatureEntry.setStatus("current")
_RuijieSystemTemperatureIndex_Type = Integer32
_RuijieSystemTemperatureIndex_Object = MibTableColumn
ruijieSystemTemperatureIndex = _RuijieSystemTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23, 1, 1),
    _RuijieSystemTemperatureIndex_Type()
)
ruijieSystemTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemTemperatureIndex.setStatus("current")
_RuijieSystemTemperatureName_Type = DisplayString
_RuijieSystemTemperatureName_Object = MibTableColumn
ruijieSystemTemperatureName = _RuijieSystemTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23, 1, 2),
    _RuijieSystemTemperatureName_Type()
)
ruijieSystemTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemTemperatureName.setStatus("current")
_RuijieSystemTemperatureCurrent_Type = Integer32
_RuijieSystemTemperatureCurrent_Object = MibTableColumn
ruijieSystemTemperatureCurrent = _RuijieSystemTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23, 1, 3),
    _RuijieSystemTemperatureCurrent_Type()
)
ruijieSystemTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemTemperatureCurrent.setStatus("current")
_RuijieSystemTemperatureWarningVaule_Type = Integer32
_RuijieSystemTemperatureWarningVaule_Object = MibTableColumn
ruijieSystemTemperatureWarningVaule = _RuijieSystemTemperatureWarningVaule_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23, 1, 4),
    _RuijieSystemTemperatureWarningVaule_Type()
)
ruijieSystemTemperatureWarningVaule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemTemperatureWarningVaule.setStatus("current")
_RuijieSystemTemperatureCritialVaule_Type = Integer32
_RuijieSystemTemperatureCritialVaule_Object = MibTableColumn
ruijieSystemTemperatureCritialVaule = _RuijieSystemTemperatureCritialVaule_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 23, 1, 5),
    _RuijieSystemTemperatureCritialVaule_Type()
)
ruijieSystemTemperatureCritialVaule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemTemperatureCritialVaule.setStatus("current")
_RuijieSystemSerialno_Type = DisplayString
_RuijieSystemSerialno_Object = MibScalar
ruijieSystemSerialno = _RuijieSystemSerialno_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 24),
    _RuijieSystemSerialno_Type()
)
ruijieSystemSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSerialno.setStatus("current")
_RuijieSystemVersionTable_Object = MibTable
ruijieSystemVersionTable = _RuijieSystemVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25)
)
if mibBuilder.loadTexts:
    ruijieSystemVersionTable.setStatus("current")
_RuijieSystemVersionEntry_Object = MibTableRow
ruijieSystemVersionEntry = _RuijieSystemVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1)
)
ruijieSystemVersionEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemVersionIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemVersionEntry.setStatus("current")
_RuijieSystemVersionIndex_Type = Unsigned32
_RuijieSystemVersionIndex_Object = MibTableColumn
ruijieSystemVersionIndex = _RuijieSystemVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 1),
    _RuijieSystemVersionIndex_Type()
)
ruijieSystemVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionIndex.setStatus("current")
_RuijieSystemVersionName_Type = DisplayString
_RuijieSystemVersionName_Object = MibTableColumn
ruijieSystemVersionName = _RuijieSystemVersionName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 2),
    _RuijieSystemVersionName_Type()
)
ruijieSystemVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionName.setStatus("current")
_RuijieSystemVersionSwBoot_Type = DisplayString
_RuijieSystemVersionSwBoot_Object = MibTableColumn
ruijieSystemVersionSwBoot = _RuijieSystemVersionSwBoot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 3),
    _RuijieSystemVersionSwBoot_Type()
)
ruijieSystemVersionSwBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionSwBoot.setStatus("current")
_RuijieSystemVersionSwCtrl_Type = DisplayString
_RuijieSystemVersionSwCtrl_Object = MibTableColumn
ruijieSystemVersionSwCtrl = _RuijieSystemVersionSwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 4),
    _RuijieSystemVersionSwCtrl_Type()
)
ruijieSystemVersionSwCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionSwCtrl.setStatus("current")
_RuijieSystemVersionSwMain_Type = DisplayString
_RuijieSystemVersionSwMain_Object = MibTableColumn
ruijieSystemVersionSwMain = _RuijieSystemVersionSwMain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 5),
    _RuijieSystemVersionSwMain_Type()
)
ruijieSystemVersionSwMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionSwMain.setStatus("current")
_RuijieSystemVersionHw_Type = DisplayString
_RuijieSystemVersionHw_Object = MibTableColumn
ruijieSystemVersionHw = _RuijieSystemVersionHw_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 6),
    _RuijieSystemVersionHw_Type()
)
ruijieSystemVersionHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionHw.setStatus("current")
_RuijieSystemVersionSerialno_Type = DisplayString
_RuijieSystemVersionSerialno_Object = MibTableColumn
ruijieSystemVersionSerialno = _RuijieSystemVersionSerialno_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 25, 1, 7),
    _RuijieSystemVersionSerialno_Type()
)
ruijieSystemVersionSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemVersionSerialno.setStatus("current")
_RuijieSystemSysModel_Type = DisplayString
_RuijieSystemSysModel_Object = MibScalar
ruijieSystemSysModel = _RuijieSystemSysModel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 26),
    _RuijieSystemSysModel_Type()
)
ruijieSystemSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSysModel.setStatus("current")
_RuijieSystemUptime_Type = Integer32
_RuijieSystemUptime_Object = MibScalar
ruijieSystemUptime = _RuijieSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 27),
    _RuijieSystemUptime_Type()
)
ruijieSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemUptime.setStatus("current")
_RuijieSystemSampleTime_Type = Integer32
_RuijieSystemSampleTime_Object = MibScalar
ruijieSystemSampleTime = _RuijieSystemSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 28),
    _RuijieSystemSampleTime_Type()
)
ruijieSystemSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemSampleTime.setStatus("current")
_RuijieSystemStatWindowTime_Type = Integer32
_RuijieSystemStatWindowTime_Object = MibScalar
ruijieSystemStatWindowTime = _RuijieSystemStatWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 29),
    _RuijieSystemStatWindowTime_Type()
)
ruijieSystemStatWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemStatWindowTime.setStatus("current")
_RuijieSystemManufacturer_Type = DisplayString
_RuijieSystemManufacturer_Object = MibScalar
ruijieSystemManufacturer = _RuijieSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 30),
    _RuijieSystemManufacturer_Type()
)
ruijieSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemManufacturer.setStatus("current")
_RuijieSystemCurrentTime_Type = DisplayString
_RuijieSystemCurrentTime_Object = MibScalar
ruijieSystemCurrentTime = _RuijieSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 31),
    _RuijieSystemCurrentTime_Type()
)
ruijieSystemCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemCurrentTime.setStatus("current")
_RuijieSystemWarnResendTime_Type = Integer32
_RuijieSystemWarnResendTime_Object = MibScalar
ruijieSystemWarnResendTime = _RuijieSystemWarnResendTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 32),
    _RuijieSystemWarnResendTime_Type()
)
ruijieSystemWarnResendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemWarnResendTime.setStatus("current")
_RuijieSystemSoftwareName_Type = DisplayString
_RuijieSystemSoftwareName_Object = MibScalar
ruijieSystemSoftwareName = _RuijieSystemSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 33),
    _RuijieSystemSoftwareName_Type()
)
ruijieSystemSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSoftwareName.setStatus("current")
_RuijieSystemSoftwareManufacturer_Type = DisplayString
_RuijieSystemSoftwareManufacturer_Object = MibScalar
ruijieSystemSoftwareManufacturer = _RuijieSystemSoftwareManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 34),
    _RuijieSystemSoftwareManufacturer_Type()
)
ruijieSystemSoftwareManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSoftwareManufacturer.setStatus("current")
_RuijieSystemCpuType_Type = DisplayString
_RuijieSystemCpuType_Object = MibScalar
ruijieSystemCpuType = _RuijieSystemCpuType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 35),
    _RuijieSystemCpuType_Type()
)
ruijieSystemCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemCpuType.setStatus("current")
_RuijieSystemMemoryType_Type = DisplayString
_RuijieSystemMemoryType_Object = MibScalar
ruijieSystemMemoryType = _RuijieSystemMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 36),
    _RuijieSystemMemoryType_Type()
)
ruijieSystemMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMemoryType.setStatus("current")
_RuijieSystemMemorySize_Type = Gauge32
_RuijieSystemMemorySize_Object = MibScalar
ruijieSystemMemorySize = _RuijieSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 37),
    _RuijieSystemMemorySize_Type()
)
ruijieSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMemorySize.setStatus("current")
_RuijieSystemFlashSize_Type = Gauge32
_RuijieSystemFlashSize_Object = MibScalar
ruijieSystemFlashSize = _RuijieSystemFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 38),
    _RuijieSystemFlashSize_Type()
)
ruijieSystemFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFlashSize.setStatus("current")
_RuijieSystemLankApTable_Object = MibTable
ruijieSystemLankApTable = _RuijieSystemLankApTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39)
)
if mibBuilder.loadTexts:
    ruijieSystemLankApTable.setStatus("current")
_RuijieSystemLankApEntry_Object = MibTableRow
ruijieSystemLankApEntry = _RuijieSystemLankApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1)
)
ruijieSystemLankApEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemLankApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieSystemLankApEntry.setStatus("current")
_RuijieSystemLankApMacAddr_Type = MacAddress
_RuijieSystemLankApMacAddr_Object = MibTableColumn
ruijieSystemLankApMacAddr = _RuijieSystemLankApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 1),
    _RuijieSystemLankApMacAddr_Type()
)
ruijieSystemLankApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApMacAddr.setStatus("current")
_RuijieSystemLankApStatWindowTime_Type = Integer32
_RuijieSystemLankApStatWindowTime_Object = MibTableColumn
ruijieSystemLankApStatWindowTime = _RuijieSystemLankApStatWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 2),
    _RuijieSystemLankApStatWindowTime_Type()
)
ruijieSystemLankApStatWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemLankApStatWindowTime.setStatus("current")
_RuijieSystemLankApSampleTime_Type = Integer32
_RuijieSystemLankApSampleTime_Object = MibTableColumn
ruijieSystemLankApSampleTime = _RuijieSystemLankApSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 3),
    _RuijieSystemLankApSampleTime_Type()
)
ruijieSystemLankApSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemLankApSampleTime.setStatus("current")


class _RuijieSystemLankApReset_Type(Integer32):
    """Custom type ruijieSystemLankApReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("restart", 1))
    )


_RuijieSystemLankApReset_Type.__name__ = "Integer32"
_RuijieSystemLankApReset_Object = MibTableColumn
ruijieSystemLankApReset = _RuijieSystemLankApReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 4),
    _RuijieSystemLankApReset_Type()
)
ruijieSystemLankApReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemLankApReset.setStatus("current")
_RuijieSystemLankApSoftwareName_Type = DisplayString
_RuijieSystemLankApSoftwareName_Object = MibTableColumn
ruijieSystemLankApSoftwareName = _RuijieSystemLankApSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 5),
    _RuijieSystemLankApSoftwareName_Type()
)
ruijieSystemLankApSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApSoftwareName.setStatus("current")


class _RuijieSystemLankApSwVersion_Type(DisplayString):
    """Custom type ruijieSystemLankApSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSystemLankApSwVersion_Type.__name__ = "DisplayString"
_RuijieSystemLankApSwVersion_Object = MibTableColumn
ruijieSystemLankApSwVersion = _RuijieSystemLankApSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 6),
    _RuijieSystemLankApSwVersion_Type()
)
ruijieSystemLankApSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApSwVersion.setStatus("current")
_RuijieSystemLankApSoftwareManufacturer_Type = DisplayString
_RuijieSystemLankApSoftwareManufacturer_Object = MibTableColumn
ruijieSystemLankApSoftwareManufacturer = _RuijieSystemLankApSoftwareManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 7),
    _RuijieSystemLankApSoftwareManufacturer_Type()
)
ruijieSystemLankApSoftwareManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApSoftwareManufacturer.setStatus("current")
_RuijieSystemLankApCpuType_Type = DisplayString
_RuijieSystemLankApCpuType_Object = MibTableColumn
ruijieSystemLankApCpuType = _RuijieSystemLankApCpuType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 8),
    _RuijieSystemLankApCpuType_Type()
)
ruijieSystemLankApCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApCpuType.setStatus("current")
_RuijieSystemLankApMemoryType_Type = DisplayString
_RuijieSystemLankApMemoryType_Object = MibTableColumn
ruijieSystemLankApMemoryType = _RuijieSystemLankApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 9),
    _RuijieSystemLankApMemoryType_Type()
)
ruijieSystemLankApMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApMemoryType.setStatus("current")
_RuijieSystemLankApMemorySize_Type = Gauge32
_RuijieSystemLankApMemorySize_Object = MibTableColumn
ruijieSystemLankApMemorySize = _RuijieSystemLankApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 10),
    _RuijieSystemLankApMemorySize_Type()
)
ruijieSystemLankApMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApMemorySize.setStatus("current")
_RuijieSystemLankAPFlashSize_Type = Gauge32
_RuijieSystemLankAPFlashSize_Object = MibTableColumn
ruijieSystemLankAPFlashSize = _RuijieSystemLankAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 11),
    _RuijieSystemLankAPFlashSize_Type()
)
ruijieSystemLankAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankAPFlashSize.setStatus("current")
_RuijieSystemLankApManufacturer_Type = DisplayString
_RuijieSystemLankApManufacturer_Object = MibTableColumn
ruijieSystemLankApManufacturer = _RuijieSystemLankApManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 12),
    _RuijieSystemLankApManufacturer_Type()
)
ruijieSystemLankApManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApManufacturer.setStatus("current")
_RuijieSystemLankApSerialno_Type = DisplayString
_RuijieSystemLankApSerialno_Object = MibTableColumn
ruijieSystemLankApSerialno = _RuijieSystemLankApSerialno_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 13),
    _RuijieSystemLankApSerialno_Type()
)
ruijieSystemLankApSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApSerialno.setStatus("current")
_RuijieSystemLankApSysModel_Type = DisplayString
_RuijieSystemLankApSysModel_Object = MibTableColumn
ruijieSystemLankApSysModel = _RuijieSystemLankApSysModel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 14),
    _RuijieSystemLankApSysModel_Type()
)
ruijieSystemLankApSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApSysModel.setStatus("current")
_RuijieSystemLankApUptime_Type = Integer32
_RuijieSystemLankApUptime_Object = MibTableColumn
ruijieSystemLankApUptime = _RuijieSystemLankApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 15),
    _RuijieSystemLankApUptime_Type()
)
ruijieSystemLankApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApUptime.setStatus("current")
_RuijieSystemLankApAccurateUptime_Type = TimeTicks
_RuijieSystemLankApAccurateUptime_Object = MibTableColumn
ruijieSystemLankApAccurateUptime = _RuijieSystemLankApAccurateUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 16),
    _RuijieSystemLankApAccurateUptime_Type()
)
ruijieSystemLankApAccurateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApAccurateUptime.setStatus("current")


class _RuijieSystemLankApHwVersion_Type(DisplayString):
    """Custom type ruijieSystemLankApHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSystemLankApHwVersion_Type.__name__ = "DisplayString"
_RuijieSystemLankApHwVersion_Object = MibTableColumn
ruijieSystemLankApHwVersion = _RuijieSystemLankApHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 39, 1, 17),
    _RuijieSystemLankApHwVersion_Type()
)
ruijieSystemLankApHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemLankApHwVersion.setStatus("current")
_RuijieSystemBoardTemperatureTable_Object = MibTable
ruijieSystemBoardTemperatureTable = _RuijieSystemBoardTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 40)
)
if mibBuilder.loadTexts:
    ruijieSystemBoardTemperatureTable.setStatus("current")
_RuijieSystemBoardTemperatureEntry_Object = MibTableRow
ruijieSystemBoardTemperatureEntry = _RuijieSystemBoardTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 40, 1)
)
ruijieSystemBoardTemperatureEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemBoardTemperatureIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemBoardTemperatureEntry.setStatus("current")
_RuijieSystemBoardTemperatureIndex_Type = Integer32
_RuijieSystemBoardTemperatureIndex_Object = MibTableColumn
ruijieSystemBoardTemperatureIndex = _RuijieSystemBoardTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 40, 1, 1),
    _RuijieSystemBoardTemperatureIndex_Type()
)
ruijieSystemBoardTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemBoardTemperatureIndex.setStatus("current")
_RuijieSystemBoardTemperatureName_Type = DisplayString
_RuijieSystemBoardTemperatureName_Object = MibTableColumn
ruijieSystemBoardTemperatureName = _RuijieSystemBoardTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 40, 1, 2),
    _RuijieSystemBoardTemperatureName_Type()
)
ruijieSystemBoardTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemBoardTemperatureName.setStatus("current")
_RuijieSystemBoardTemperatureCurrent_Type = Integer32
_RuijieSystemBoardTemperatureCurrent_Object = MibTableColumn
ruijieSystemBoardTemperatureCurrent = _RuijieSystemBoardTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 40, 1, 3),
    _RuijieSystemBoardTemperatureCurrent_Type()
)
ruijieSystemBoardTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemBoardTemperatureCurrent.setStatus("current")
_RuijieSystemElectricalInformationTable_Object = MibTable
ruijieSystemElectricalInformationTable = _RuijieSystemElectricalInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41)
)
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationTable.setStatus("current")
_RuijieSystemElectricalInformationEntry_Object = MibTableRow
ruijieSystemElectricalInformationEntry = _RuijieSystemElectricalInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1)
)
ruijieSystemElectricalInformationEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemElectricalInformationDeviceIndex"),
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemElectricalInformationIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationEntry.setStatus("current")
_RuijieSystemElectricalInformationDeviceIndex_Type = Integer32
_RuijieSystemElectricalInformationDeviceIndex_Object = MibTableColumn
ruijieSystemElectricalInformationDeviceIndex = _RuijieSystemElectricalInformationDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 1),
    _RuijieSystemElectricalInformationDeviceIndex_Type()
)
ruijieSystemElectricalInformationDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationDeviceIndex.setStatus("current")
_RuijieSystemElectricalInformationIndex_Type = Integer32
_RuijieSystemElectricalInformationIndex_Object = MibTableColumn
ruijieSystemElectricalInformationIndex = _RuijieSystemElectricalInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 2),
    _RuijieSystemElectricalInformationIndex_Type()
)
ruijieSystemElectricalInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationIndex.setStatus("current")


class _RuijieSystemElectricalInformationStatus_Type(Integer32):
    """Custom type ruijieSystemElectricalInformationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_RuijieSystemElectricalInformationStatus_Type.__name__ = "Integer32"
_RuijieSystemElectricalInformationStatus_Object = MibTableColumn
ruijieSystemElectricalInformationStatus = _RuijieSystemElectricalInformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 3),
    _RuijieSystemElectricalInformationStatus_Type()
)
ruijieSystemElectricalInformationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationStatus.setStatus("current")
_RuijieSystemElectricalInformationType_Type = DisplayString
_RuijieSystemElectricalInformationType_Object = MibTableColumn
ruijieSystemElectricalInformationType = _RuijieSystemElectricalInformationType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 4),
    _RuijieSystemElectricalInformationType_Type()
)
ruijieSystemElectricalInformationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationType.setStatus("current")
_RuijieSystemElectricalInformationAttribute_Type = DisplayString
_RuijieSystemElectricalInformationAttribute_Object = MibTableColumn
ruijieSystemElectricalInformationAttribute = _RuijieSystemElectricalInformationAttribute_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 5),
    _RuijieSystemElectricalInformationAttribute_Type()
)
ruijieSystemElectricalInformationAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationAttribute.setStatus("current")
_RuijieSystemElectricalInformationSofeVersion_Type = DisplayString
_RuijieSystemElectricalInformationSofeVersion_Object = MibTableColumn
ruijieSystemElectricalInformationSofeVersion = _RuijieSystemElectricalInformationSofeVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 6),
    _RuijieSystemElectricalInformationSofeVersion_Type()
)
ruijieSystemElectricalInformationSofeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationSofeVersion.setStatus("current")
_RuijieSystemElectricalInformationHardwareVersion_Type = DisplayString
_RuijieSystemElectricalInformationHardwareVersion_Object = MibTableColumn
ruijieSystemElectricalInformationHardwareVersion = _RuijieSystemElectricalInformationHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 7),
    _RuijieSystemElectricalInformationHardwareVersion_Type()
)
ruijieSystemElectricalInformationHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationHardwareVersion.setStatus("current")
_RuijieSystemElectricalInformationSerial_Type = DisplayString
_RuijieSystemElectricalInformationSerial_Object = MibTableColumn
ruijieSystemElectricalInformationSerial = _RuijieSystemElectricalInformationSerial_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 8),
    _RuijieSystemElectricalInformationSerial_Type()
)
ruijieSystemElectricalInformationSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationSerial.setStatus("current")
_RuijieSystemElectricalInformationProductionDate_Type = DisplayString
_RuijieSystemElectricalInformationProductionDate_Object = MibTableColumn
ruijieSystemElectricalInformationProductionDate = _RuijieSystemElectricalInformationProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 9),
    _RuijieSystemElectricalInformationProductionDate_Type()
)
ruijieSystemElectricalInformationProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationProductionDate.setStatus("current")
_RuijieSystemElectricalInformationRatedPower_Type = Integer32
_RuijieSystemElectricalInformationRatedPower_Object = MibTableColumn
ruijieSystemElectricalInformationRatedPower = _RuijieSystemElectricalInformationRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 10),
    _RuijieSystemElectricalInformationRatedPower_Type()
)
ruijieSystemElectricalInformationRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationRatedPower.setStatus("current")
_RuijieSystemElectricalInformationInVoltage_Type = Integer32
_RuijieSystemElectricalInformationInVoltage_Object = MibTableColumn
ruijieSystemElectricalInformationInVoltage = _RuijieSystemElectricalInformationInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 11),
    _RuijieSystemElectricalInformationInVoltage_Type()
)
ruijieSystemElectricalInformationInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationInVoltage.setStatus("current")
_RuijieSystemElectricalInformationInCurrent_Type = Integer32
_RuijieSystemElectricalInformationInCurrent_Object = MibTableColumn
ruijieSystemElectricalInformationInCurrent = _RuijieSystemElectricalInformationInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 12),
    _RuijieSystemElectricalInformationInCurrent_Type()
)
ruijieSystemElectricalInformationInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationInCurrent.setStatus("current")
_RuijieSystemElectricalInformationOutVoltage_Type = Integer32
_RuijieSystemElectricalInformationOutVoltage_Object = MibTableColumn
ruijieSystemElectricalInformationOutVoltage = _RuijieSystemElectricalInformationOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 13),
    _RuijieSystemElectricalInformationOutVoltage_Type()
)
ruijieSystemElectricalInformationOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationOutVoltage.setStatus("current")
_RuijieSystemElectricalInformationOutCurrent_Type = Integer32
_RuijieSystemElectricalInformationOutCurrent_Object = MibTableColumn
ruijieSystemElectricalInformationOutCurrent = _RuijieSystemElectricalInformationOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 14),
    _RuijieSystemElectricalInformationOutCurrent_Type()
)
ruijieSystemElectricalInformationOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationOutCurrent.setStatus("current")
_RuijieSystemElectricalInformationOutPower_Type = Integer32
_RuijieSystemElectricalInformationOutPower_Object = MibTableColumn
ruijieSystemElectricalInformationOutPower = _RuijieSystemElectricalInformationOutPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 15),
    _RuijieSystemElectricalInformationOutPower_Type()
)
ruijieSystemElectricalInformationOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationOutPower.setStatus("current")
_RuijieSystemElectricalInformationTemperature_Type = Integer32
_RuijieSystemElectricalInformationTemperature_Object = MibTableColumn
ruijieSystemElectricalInformationTemperature = _RuijieSystemElectricalInformationTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 16),
    _RuijieSystemElectricalInformationTemperature_Type()
)
ruijieSystemElectricalInformationTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationTemperature.setStatus("current")
_RuijieSystemElectricalInformationAirflowCoexist_Type = DisplayString
_RuijieSystemElectricalInformationAirflowCoexist_Object = MibTableColumn
ruijieSystemElectricalInformationAirflowCoexist = _RuijieSystemElectricalInformationAirflowCoexist_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 17),
    _RuijieSystemElectricalInformationAirflowCoexist_Type()
)
ruijieSystemElectricalInformationAirflowCoexist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationAirflowCoexist.setStatus("current")
_RuijieSystemElectricalInformationWarningStatus_Type = DisplayString
_RuijieSystemElectricalInformationWarningStatus_Object = MibTableColumn
ruijieSystemElectricalInformationWarningStatus = _RuijieSystemElectricalInformationWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 41, 1, 18),
    _RuijieSystemElectricalInformationWarningStatus_Type()
)
ruijieSystemElectricalInformationWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemElectricalInformationWarningStatus.setStatus("current")
_RuijieSystemFanInformationTable_Object = MibTable
ruijieSystemFanInformationTable = _RuijieSystemFanInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42)
)
if mibBuilder.loadTexts:
    ruijieSystemFanInformationTable.setStatus("current")
_RuijieSystemFanInformationEntry_Object = MibTableRow
ruijieSystemFanInformationEntry = _RuijieSystemFanInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1)
)
ruijieSystemFanInformationEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanInformationDeviceIndex"),
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanInformationFanIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanInformationEntry.setStatus("current")
_RuijieSystemFanInformationDeviceIndex_Type = Integer32
_RuijieSystemFanInformationDeviceIndex_Object = MibTableColumn
ruijieSystemFanInformationDeviceIndex = _RuijieSystemFanInformationDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 1),
    _RuijieSystemFanInformationDeviceIndex_Type()
)
ruijieSystemFanInformationDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationDeviceIndex.setStatus("current")
_RuijieSystemFanInformationFanIndex_Type = Integer32
_RuijieSystemFanInformationFanIndex_Object = MibTableColumn
ruijieSystemFanInformationFanIndex = _RuijieSystemFanInformationFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 2),
    _RuijieSystemFanInformationFanIndex_Type()
)
ruijieSystemFanInformationFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationFanIndex.setStatus("current")


class _RuijieSystemFanInformationStatus_Type(Integer32):
    """Custom type ruijieSystemFanInformationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6),
          ("linefail", 7))
    )


_RuijieSystemFanInformationStatus_Type.__name__ = "Integer32"
_RuijieSystemFanInformationStatus_Object = MibTableColumn
ruijieSystemFanInformationStatus = _RuijieSystemFanInformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 3),
    _RuijieSystemFanInformationStatus_Type()
)
ruijieSystemFanInformationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationStatus.setStatus("current")
_RuijieSystemFanInformationType_Type = DisplayString
_RuijieSystemFanInformationType_Object = MibTableColumn
ruijieSystemFanInformationType = _RuijieSystemFanInformationType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 4),
    _RuijieSystemFanInformationType_Type()
)
ruijieSystemFanInformationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationType.setStatus("current")
_RuijieSystemFanInformationAttribute_Type = DisplayString
_RuijieSystemFanInformationAttribute_Object = MibTableColumn
ruijieSystemFanInformationAttribute = _RuijieSystemFanInformationAttribute_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 5),
    _RuijieSystemFanInformationAttribute_Type()
)
ruijieSystemFanInformationAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationAttribute.setStatus("current")
_RuijieSystemFanInformationSofeVersion_Type = DisplayString
_RuijieSystemFanInformationSofeVersion_Object = MibTableColumn
ruijieSystemFanInformationSofeVersion = _RuijieSystemFanInformationSofeVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 6),
    _RuijieSystemFanInformationSofeVersion_Type()
)
ruijieSystemFanInformationSofeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationSofeVersion.setStatus("current")
_RuijieSystemFanInformationFirmwareVersion_Type = DisplayString
_RuijieSystemFanInformationFirmwareVersion_Object = MibTableColumn
ruijieSystemFanInformationFirmwareVersion = _RuijieSystemFanInformationFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 7),
    _RuijieSystemFanInformationFirmwareVersion_Type()
)
ruijieSystemFanInformationFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationFirmwareVersion.setStatus("current")
_RuijieSystemFanInformationHardwareVersion_Type = DisplayString
_RuijieSystemFanInformationHardwareVersion_Object = MibTableColumn
ruijieSystemFanInformationHardwareVersion = _RuijieSystemFanInformationHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 8),
    _RuijieSystemFanInformationHardwareVersion_Type()
)
ruijieSystemFanInformationHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationHardwareVersion.setStatus("current")
_RuijieSystemFanInformationSerial_Type = DisplayString
_RuijieSystemFanInformationSerial_Object = MibTableColumn
ruijieSystemFanInformationSerial = _RuijieSystemFanInformationSerial_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 9),
    _RuijieSystemFanInformationSerial_Type()
)
ruijieSystemFanInformationSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationSerial.setStatus("current")
_RuijieSystemFanInformationProductionDate_Type = DisplayString
_RuijieSystemFanInformationProductionDate_Object = MibTableColumn
ruijieSystemFanInformationProductionDate = _RuijieSystemFanInformationProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 10),
    _RuijieSystemFanInformationProductionDate_Type()
)
ruijieSystemFanInformationProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationProductionDate.setStatus("current")
_RuijieSystemFanInformationTemperature_Type = Integer32
_RuijieSystemFanInformationTemperature_Object = MibTableColumn
ruijieSystemFanInformationTemperature = _RuijieSystemFanInformationTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 11),
    _RuijieSystemFanInformationTemperature_Type()
)
ruijieSystemFanInformationTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationTemperature.setStatus("current")
_RuijieSystemFanInformationNumber_Type = Integer32
_RuijieSystemFanInformationNumber_Object = MibTableColumn
ruijieSystemFanInformationNumber = _RuijieSystemFanInformationNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 12),
    _RuijieSystemFanInformationNumber_Type()
)
ruijieSystemFanInformationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationNumber.setStatus("current")
_RuijieSystemFanInformationAirflowCoexist_Type = DisplayString
_RuijieSystemFanInformationAirflowCoexist_Object = MibTableColumn
ruijieSystemFanInformationAirflowCoexist = _RuijieSystemFanInformationAirflowCoexist_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 13),
    _RuijieSystemFanInformationAirflowCoexist_Type()
)
ruijieSystemFanInformationAirflowCoexist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationAirflowCoexist.setStatus("current")
_RuijieSystemFanInformationWarningStatus_Type = DisplayString
_RuijieSystemFanInformationWarningStatus_Object = MibTableColumn
ruijieSystemFanInformationWarningStatus = _RuijieSystemFanInformationWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 42, 1, 14),
    _RuijieSystemFanInformationWarningStatus_Type()
)
ruijieSystemFanInformationWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanInformationWarningStatus.setStatus("current")
_RuijieSystemFanStatusTable_Object = MibTable
ruijieSystemFanStatusTable = _RuijieSystemFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43)
)
if mibBuilder.loadTexts:
    ruijieSystemFanStatusTable.setStatus("current")
_RuijieSystemFanStatusEntry_Object = MibTableRow
ruijieSystemFanStatusEntry = _RuijieSystemFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1)
)
ruijieSystemFanStatusEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusDeviceIndex"),
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanStatusEntry.setStatus("current")
_RuijieSystemFanStatusDeviceIndex_Type = Integer32
_RuijieSystemFanStatusDeviceIndex_Object = MibTableColumn
ruijieSystemFanStatusDeviceIndex = _RuijieSystemFanStatusDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1, 1),
    _RuijieSystemFanStatusDeviceIndex_Type()
)
ruijieSystemFanStatusDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanStatusDeviceIndex.setStatus("current")
_RuijieSystemFanStatusFanIndex_Type = Integer32
_RuijieSystemFanStatusFanIndex_Object = MibTableColumn
ruijieSystemFanStatusFanIndex = _RuijieSystemFanStatusFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1, 2),
    _RuijieSystemFanStatusFanIndex_Type()
)
ruijieSystemFanStatusFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanStatusFanIndex.setStatus("current")
_RuijieSystemFanStatusIndex_Type = Integer32
_RuijieSystemFanStatusIndex_Object = MibTableColumn
ruijieSystemFanStatusIndex = _RuijieSystemFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1, 3),
    _RuijieSystemFanStatusIndex_Type()
)
ruijieSystemFanStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanStatusIndex.setStatus("current")


class _RuijieSystemFanStatus_Type(Integer32):
    """Custom type ruijieSystemFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noexist", 1),
          ("existnopower", 2),
          ("existreadypower", 3),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_RuijieSystemFanStatus_Type.__name__ = "Integer32"
_RuijieSystemFanStatus_Object = MibTableColumn
ruijieSystemFanStatus = _RuijieSystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1, 4),
    _RuijieSystemFanStatus_Type()
)
ruijieSystemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanStatus.setStatus("current")
_RuijieSystemFanStatusLevel_Type = Integer32
_RuijieSystemFanStatusLevel_Object = MibTableColumn
ruijieSystemFanStatusLevel = _RuijieSystemFanStatusLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1, 5),
    _RuijieSystemFanStatusLevel_Type()
)
ruijieSystemFanStatusLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanStatusLevel.setStatus("current")
_RuijieSystemFanStatusSpeed_Type = Integer32
_RuijieSystemFanStatusSpeed_Object = MibTableColumn
ruijieSystemFanStatusSpeed = _RuijieSystemFanStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 43, 1, 6),
    _RuijieSystemFanStatusSpeed_Type()
)
ruijieSystemFanStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanStatusSpeed.setStatus("current")
_RuijieSystemMultipleTemperatureTable_Object = MibTable
ruijieSystemMultipleTemperatureTable = _RuijieSystemMultipleTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44)
)
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureTable.setStatus("current")
_RuijieSystemMultipleTemperatureEntry_Object = MibTableRow
ruijieSystemMultipleTemperatureEntry = _RuijieSystemMultipleTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1)
)
ruijieSystemMultipleTemperatureEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureDeviceIndex"),
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureSlotIndex"),
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureEntry.setStatus("current")
_RuijieSystemMultipleTemperatureDeviceIndex_Type = Integer32
_RuijieSystemMultipleTemperatureDeviceIndex_Object = MibTableColumn
ruijieSystemMultipleTemperatureDeviceIndex = _RuijieSystemMultipleTemperatureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 1),
    _RuijieSystemMultipleTemperatureDeviceIndex_Type()
)
ruijieSystemMultipleTemperatureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureDeviceIndex.setStatus("current")
_RuijieSystemMultipleTemperatureSlotIndex_Type = Integer32
_RuijieSystemMultipleTemperatureSlotIndex_Object = MibTableColumn
ruijieSystemMultipleTemperatureSlotIndex = _RuijieSystemMultipleTemperatureSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 2),
    _RuijieSystemMultipleTemperatureSlotIndex_Type()
)
ruijieSystemMultipleTemperatureSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureSlotIndex.setStatus("current")
_RuijieSystemMultipleTemperatureIndex_Type = Integer32
_RuijieSystemMultipleTemperatureIndex_Object = MibTableColumn
ruijieSystemMultipleTemperatureIndex = _RuijieSystemMultipleTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 3),
    _RuijieSystemMultipleTemperatureIndex_Type()
)
ruijieSystemMultipleTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureIndex.setStatus("current")
_RuijieSystemMultipleTemperatureName_Type = DisplayString
_RuijieSystemMultipleTemperatureName_Object = MibTableColumn
ruijieSystemMultipleTemperatureName = _RuijieSystemMultipleTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 4),
    _RuijieSystemMultipleTemperatureName_Type()
)
ruijieSystemMultipleTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureName.setStatus("current")
_RuijieSystemMultipleTemperatureCurrent_Type = Integer32
_RuijieSystemMultipleTemperatureCurrent_Object = MibTableColumn
ruijieSystemMultipleTemperatureCurrent = _RuijieSystemMultipleTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 5),
    _RuijieSystemMultipleTemperatureCurrent_Type()
)
ruijieSystemMultipleTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureCurrent.setStatus("current")
_RuijieSystemMultipleTemperatureWarning_Type = Integer32
_RuijieSystemMultipleTemperatureWarning_Object = MibTableColumn
ruijieSystemMultipleTemperatureWarning = _RuijieSystemMultipleTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 6),
    _RuijieSystemMultipleTemperatureWarning_Type()
)
ruijieSystemMultipleTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureWarning.setStatus("current")
_RuijieSystemMultipleTemperatureCritical_Type = Integer32
_RuijieSystemMultipleTemperatureCritical_Object = MibTableColumn
ruijieSystemMultipleTemperatureCritical = _RuijieSystemMultipleTemperatureCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 44, 1, 7),
    _RuijieSystemMultipleTemperatureCritical_Type()
)
ruijieSystemMultipleTemperatureCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemMultipleTemperatureCritical.setStatus("current")
_RuijieSystemAccurateUptime_Type = TimeTicks
_RuijieSystemAccurateUptime_Object = MibScalar
ruijieSystemAccurateUptime = _RuijieSystemAccurateUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 45),
    _RuijieSystemAccurateUptime_Type()
)
ruijieSystemAccurateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemAccurateUptime.setStatus("current")
_RuijieSystemPowerIndex_Type = Integer32
_RuijieSystemPowerIndex_Object = MibScalar
ruijieSystemPowerIndex = _RuijieSystemPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 46),
    _RuijieSystemPowerIndex_Type()
)
ruijieSystemPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemPowerIndex.setStatus("current")
_RuijieSystemSwitchID_Type = Integer32
_RuijieSystemSwitchID_Object = MibScalar
ruijieSystemSwitchID = _RuijieSystemSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 47),
    _RuijieSystemSwitchID_Type()
)
ruijieSystemSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemSwitchID.setStatus("current")
_RuijieSystemApDeviceDescriptionTable_Object = MibTable
ruijieSystemApDeviceDescriptionTable = _RuijieSystemApDeviceDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48)
)
if mibBuilder.loadTexts:
    ruijieSystemApDeviceDescriptionTable.setStatus("current")
_RuijieSystemApDeviceDescriptionEntry_Object = MibTableRow
ruijieSystemApDeviceDescriptionEntry = _RuijieSystemApDeviceDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1)
)
ruijieSystemApDeviceDescriptionEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemApDescMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieSystemApDeviceDescriptionEntry.setStatus("current")
_RuijieSystemApDescMacAddr_Type = MacAddress
_RuijieSystemApDescMacAddr_Object = MibTableColumn
ruijieSystemApDescMacAddr = _RuijieSystemApDescMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 1),
    _RuijieSystemApDescMacAddr_Type()
)
ruijieSystemApDescMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApDescMacAddr.setStatus("current")


class _RuijieSystemApMemoryType_Type(Integer32):
    """Custom type ruijieSystemApMemoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("sdram", 1),
          ("ddram", 2))
    )


_RuijieSystemApMemoryType_Type.__name__ = "Integer32"
_RuijieSystemApMemoryType_Object = MibTableColumn
ruijieSystemApMemoryType = _RuijieSystemApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 2),
    _RuijieSystemApMemoryType_Type()
)
ruijieSystemApMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApMemoryType.setStatus("current")
_RuijieSystemApMemorySize_Type = Gauge32
_RuijieSystemApMemorySize_Object = MibTableColumn
ruijieSystemApMemorySize = _RuijieSystemApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 3),
    _RuijieSystemApMemorySize_Type()
)
ruijieSystemApMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApMemorySize.setStatus("current")


class _RuijieSystemAPFlashType_Type(Integer32):
    """Custom type ruijieSystemAPFlashType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("nor", 1),
          ("non-nor", 2))
    )


_RuijieSystemAPFlashType_Type.__name__ = "Integer32"
_RuijieSystemAPFlashType_Object = MibTableColumn
ruijieSystemAPFlashType = _RuijieSystemAPFlashType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 4),
    _RuijieSystemAPFlashType_Type()
)
ruijieSystemAPFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemAPFlashType.setStatus("current")
_RuijieSystemAPFlashSize_Type = Gauge32
_RuijieSystemAPFlashSize_Object = MibTableColumn
ruijieSystemAPFlashSize = _RuijieSystemAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 5),
    _RuijieSystemAPFlashSize_Type()
)
ruijieSystemAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemAPFlashSize.setStatus("current")
_RuijieSystemApNVRAMSize_Type = Gauge32
_RuijieSystemApNVRAMSize_Object = MibTableColumn
ruijieSystemApNVRAMSize = _RuijieSystemApNVRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 6),
    _RuijieSystemApNVRAMSize_Type()
)
ruijieSystemApNVRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApNVRAMSize.setStatus("current")
_RuijieSystemApCFSize_Type = Gauge32
_RuijieSystemApCFSize_Object = MibTableColumn
ruijieSystemApCFSize = _RuijieSystemApCFSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 7),
    _RuijieSystemApCFSize_Type()
)
ruijieSystemApCFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApCFSize.setStatus("current")
_RuijieSystemApCPUType_Type = DisplayString
_RuijieSystemApCPUType_Object = MibTableColumn
ruijieSystemApCPUType = _RuijieSystemApCPUType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 48, 1, 8),
    _RuijieSystemApCPUType_Type()
)
ruijieSystemApCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApCPUType.setStatus("current")
_RuijieSystemApDeviceStatisticsTable_Object = MibTable
ruijieSystemApDeviceStatisticsTable = _RuijieSystemApDeviceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49)
)
if mibBuilder.loadTexts:
    ruijieSystemApDeviceStatisticsTable.setStatus("current")
_RuijieSystemApDeviceStatisticsEntry_Object = MibTableRow
ruijieSystemApDeviceStatisticsEntry = _RuijieSystemApDeviceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1)
)
ruijieSystemApDeviceStatisticsEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemApStatMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieSystemApDeviceStatisticsEntry.setStatus("current")
_RuijieSystemApStatMacAddr_Type = MacAddress
_RuijieSystemApStatMacAddr_Object = MibTableColumn
ruijieSystemApStatMacAddr = _RuijieSystemApStatMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 1),
    _RuijieSystemApStatMacAddr_Type()
)
ruijieSystemApStatMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApStatMacAddr.setStatus("current")
_RuijieSystemApInterfaceNum_Type = Integer32
_RuijieSystemApInterfaceNum_Object = MibTableColumn
ruijieSystemApInterfaceNum = _RuijieSystemApInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 2),
    _RuijieSystemApInterfaceNum_Type()
)
ruijieSystemApInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApInterfaceNum.setStatus("current")
_RuijieSystemApUptime_Type = TimeTicks
_RuijieSystemApUptime_Object = MibTableColumn
ruijieSystemApUptime = _RuijieSystemApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 3),
    _RuijieSystemApUptime_Type()
)
ruijieSystemApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApUptime.setStatus("current")
_RuijieSystemApCPUUtilizationCurrent_Type = Percent
_RuijieSystemApCPUUtilizationCurrent_Object = MibTableColumn
ruijieSystemApCPUUtilizationCurrent = _RuijieSystemApCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 4),
    _RuijieSystemApCPUUtilizationCurrent_Type()
)
ruijieSystemApCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApCPUUtilizationCurrent.setStatus("current")
_RuijieSystemApCPUUtilizationAverage_Type = Percent
_RuijieSystemApCPUUtilizationAverage_Object = MibTableColumn
ruijieSystemApCPUUtilizationAverage = _RuijieSystemApCPUUtilizationAverage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 5),
    _RuijieSystemApCPUUtilizationAverage_Type()
)
ruijieSystemApCPUUtilizationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApCPUUtilizationAverage.setStatus("current")
_RuijieSystemApMemoryPoolCurrentUtilization_Type = Percent
_RuijieSystemApMemoryPoolCurrentUtilization_Object = MibTableColumn
ruijieSystemApMemoryPoolCurrentUtilization = _RuijieSystemApMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 6),
    _RuijieSystemApMemoryPoolCurrentUtilization_Type()
)
ruijieSystemApMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApMemoryPoolCurrentUtilization.setStatus("current")
_RuijieSystemApMemoryPoolAverageUtilization_Type = Percent
_RuijieSystemApMemoryPoolAverageUtilization_Object = MibTableColumn
ruijieSystemApMemoryPoolAverageUtilization = _RuijieSystemApMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 7),
    _RuijieSystemApMemoryPoolAverageUtilization_Type()
)
ruijieSystemApMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApMemoryPoolAverageUtilization.setStatus("current")
_RuijieSystemApFlashFreeSize_Type = Unsigned32
_RuijieSystemApFlashFreeSize_Object = MibTableColumn
ruijieSystemApFlashFreeSize = _RuijieSystemApFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 8),
    _RuijieSystemApFlashFreeSize_Type()
)
ruijieSystemApFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemApFlashFreeSize.setStatus("current")
_RuijieSystemAPDeviceTemperature_Type = Integer32
_RuijieSystemAPDeviceTemperature_Object = MibTableColumn
ruijieSystemAPDeviceTemperature = _RuijieSystemAPDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 49, 1, 9),
    _RuijieSystemAPDeviceTemperature_Type()
)
ruijieSystemAPDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemAPDeviceTemperature.setStatus("current")
_RuijieSystemUptimeMsLow_Type = Unsigned32
_RuijieSystemUptimeMsLow_Object = MibScalar
ruijieSystemUptimeMsLow = _RuijieSystemUptimeMsLow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 50),
    _RuijieSystemUptimeMsLow_Type()
)
ruijieSystemUptimeMsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemUptimeMsLow.setStatus("current")
_RuijieSystemUptimeMsHigh_Type = Unsigned32
_RuijieSystemUptimeMsHigh_Object = MibScalar
ruijieSystemUptimeMsHigh = _RuijieSystemUptimeMsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 51),
    _RuijieSystemUptimeMsHigh_Type()
)
ruijieSystemUptimeMsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemUptimeMsHigh.setStatus("current")
_RuijieSystemFanSNTable_Object = MibTable
ruijieSystemFanSNTable = _RuijieSystemFanSNTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 52)
)
if mibBuilder.loadTexts:
    ruijieSystemFanSNTable.setStatus("current")
_RuijieSystemFanSNEntry_Object = MibTableRow
ruijieSystemFanSNEntry = _RuijieSystemFanSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 52, 1)
)
ruijieSystemFanSNEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemFanPadIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanSNEntry.setStatus("current")
_RuijieSystemFanPadIndex_Type = Integer32
_RuijieSystemFanPadIndex_Object = MibTableColumn
ruijieSystemFanPadIndex = _RuijieSystemFanPadIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 52, 1, 1),
    _RuijieSystemFanPadIndex_Type()
)
ruijieSystemFanPadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPadIndex.setStatus("current")
_RuijieSystemFanPadName_Type = DisplayString
_RuijieSystemFanPadName_Object = MibTableColumn
ruijieSystemFanPadName = _RuijieSystemFanPadName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 52, 1, 2),
    _RuijieSystemFanPadName_Type()
)
ruijieSystemFanPadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPadName.setStatus("current")
_RuijieSystemFanPadSN_Type = DisplayString
_RuijieSystemFanPadSN_Object = MibTableColumn
ruijieSystemFanPadSN = _RuijieSystemFanPadSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 52, 1, 3),
    _RuijieSystemFanPadSN_Type()
)
ruijieSystemFanPadSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPadSN.setStatus("current")
_RuijieSystemDsfSNTable_Object = MibTable
ruijieSystemDsfSNTable = _RuijieSystemDsfSNTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 53)
)
if mibBuilder.loadTexts:
    ruijieSystemDsfSNTable.setStatus("current")
_RuijieSystemDsfSNEntry_Object = MibTableRow
ruijieSystemDsfSNEntry = _RuijieSystemDsfSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 53, 1)
)
ruijieSystemDsfSNEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemDsfIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemDsfSNEntry.setStatus("current")
_RuijieSystemDsfIndex_Type = Integer32
_RuijieSystemDsfIndex_Object = MibTableColumn
ruijieSystemDsfIndex = _RuijieSystemDsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 53, 1, 1),
    _RuijieSystemDsfIndex_Type()
)
ruijieSystemDsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemDsfIndex.setStatus("current")
_RuijieSystemDsfName_Type = DisplayString
_RuijieSystemDsfName_Object = MibTableColumn
ruijieSystemDsfName = _RuijieSystemDsfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 53, 1, 2),
    _RuijieSystemDsfName_Type()
)
ruijieSystemDsfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemDsfName.setStatus("current")
_RuijieSystemDsfSN_Type = DisplayString
_RuijieSystemDsfSN_Object = MibTableColumn
ruijieSystemDsfSN = _RuijieSystemDsfSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 53, 1, 3),
    _RuijieSystemDsfSN_Type()
)
ruijieSystemDsfSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemDsfSN.setStatus("current")
_RuijieSystemPowerSNTable_Object = MibTable
ruijieSystemPowerSNTable = _RuijieSystemPowerSNTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 54)
)
if mibBuilder.loadTexts:
    ruijieSystemPowerSNTable.setStatus("current")
_RuijieSystemPowerSNEntry_Object = MibTableRow
ruijieSystemPowerSNEntry = _RuijieSystemPowerSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 54, 1)
)
ruijieSystemPowerSNEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemPowerSNIndex"),
)
if mibBuilder.loadTexts:
    ruijieSystemPowerSNEntry.setStatus("current")
_RuijieSystemPowerSNIndex_Type = Integer32
_RuijieSystemPowerSNIndex_Object = MibTableColumn
ruijieSystemPowerSNIndex = _RuijieSystemPowerSNIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 54, 1, 1),
    _RuijieSystemPowerSNIndex_Type()
)
ruijieSystemPowerSNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemPowerSNIndex.setStatus("current")
_RuijieSystemPowerSNName_Type = DisplayString
_RuijieSystemPowerSNName_Object = MibTableColumn
ruijieSystemPowerSNName = _RuijieSystemPowerSNName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 54, 1, 2),
    _RuijieSystemPowerSNName_Type()
)
ruijieSystemPowerSNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemPowerSNName.setStatus("current")
_RuijieSystemPowerSN_Type = DisplayString
_RuijieSystemPowerSN_Object = MibTableColumn
ruijieSystemPowerSN = _RuijieSystemPowerSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 54, 1, 3),
    _RuijieSystemPowerSN_Type()
)
ruijieSystemPowerSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemPowerSN.setStatus("current")
_RuijieSystemFanPad1SpeedTable_Object = MibTable
ruijieSystemFanPad1SpeedTable = _RuijieSystemFanPad1SpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55)
)
if mibBuilder.loadTexts:
    ruijieSystemFanPad1SpeedTable.setStatus("current")
_RuijieSystemFanPad1SpeedEntry_Object = MibTableRow
ruijieSystemFanPad1SpeedEntry = _RuijieSystemFanPad1SpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1)
)
ruijieSystemFanPad1SpeedEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemOamFanPad1Index"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanPad1SpeedEntry.setStatus("current")
_RuijieSystemOamFanPad1Index_Type = Integer32
_RuijieSystemOamFanPad1Index_Object = MibTableColumn
ruijieSystemOamFanPad1Index = _RuijieSystemOamFanPad1Index_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 1),
    _RuijieSystemOamFanPad1Index_Type()
)
ruijieSystemOamFanPad1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemOamFanPad1Index.setStatus("current")
_RuijieSystemOamFanPad1Name_Type = DisplayString
_RuijieSystemOamFanPad1Name_Object = MibTableColumn
ruijieSystemOamFanPad1Name = _RuijieSystemOamFanPad1Name_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 2),
    _RuijieSystemOamFanPad1Name_Type()
)
ruijieSystemOamFanPad1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemOamFanPad1Name.setStatus("current")
_RuijieSystemFanPad1Speed1_Type = Integer32
_RuijieSystemFanPad1Speed1_Object = MibTableColumn
ruijieSystemFanPad1Speed1 = _RuijieSystemFanPad1Speed1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 3),
    _RuijieSystemFanPad1Speed1_Type()
)
ruijieSystemFanPad1Speed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed1.setStatus("current")
_RuijieSystemFanPad1Speed2_Type = Integer32
_RuijieSystemFanPad1Speed2_Object = MibTableColumn
ruijieSystemFanPad1Speed2 = _RuijieSystemFanPad1Speed2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 4),
    _RuijieSystemFanPad1Speed2_Type()
)
ruijieSystemFanPad1Speed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed2.setStatus("current")
_RuijieSystemFanPad1Speed3_Type = Integer32
_RuijieSystemFanPad1Speed3_Object = MibTableColumn
ruijieSystemFanPad1Speed3 = _RuijieSystemFanPad1Speed3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 5),
    _RuijieSystemFanPad1Speed3_Type()
)
ruijieSystemFanPad1Speed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed3.setStatus("current")
_RuijieSystemFanPad1Speed4_Type = Integer32
_RuijieSystemFanPad1Speed4_Object = MibTableColumn
ruijieSystemFanPad1Speed4 = _RuijieSystemFanPad1Speed4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 6),
    _RuijieSystemFanPad1Speed4_Type()
)
ruijieSystemFanPad1Speed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed4.setStatus("current")
_RuijieSystemFanPad1Speed5_Type = Integer32
_RuijieSystemFanPad1Speed5_Object = MibTableColumn
ruijieSystemFanPad1Speed5 = _RuijieSystemFanPad1Speed5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 7),
    _RuijieSystemFanPad1Speed5_Type()
)
ruijieSystemFanPad1Speed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed5.setStatus("current")
_RuijieSystemFanPad1Speed6_Type = Integer32
_RuijieSystemFanPad1Speed6_Object = MibTableColumn
ruijieSystemFanPad1Speed6 = _RuijieSystemFanPad1Speed6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 8),
    _RuijieSystemFanPad1Speed6_Type()
)
ruijieSystemFanPad1Speed6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed6.setStatus("current")
_RuijieSystemFanPad1Speed7_Type = Integer32
_RuijieSystemFanPad1Speed7_Object = MibTableColumn
ruijieSystemFanPad1Speed7 = _RuijieSystemFanPad1Speed7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 9),
    _RuijieSystemFanPad1Speed7_Type()
)
ruijieSystemFanPad1Speed7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed7.setStatus("current")
_RuijieSystemFanPad1Speed8_Type = Integer32
_RuijieSystemFanPad1Speed8_Object = MibTableColumn
ruijieSystemFanPad1Speed8 = _RuijieSystemFanPad1Speed8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 10),
    _RuijieSystemFanPad1Speed8_Type()
)
ruijieSystemFanPad1Speed8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed8.setStatus("current")
_RuijieSystemFanPad1Speed9_Type = Integer32
_RuijieSystemFanPad1Speed9_Object = MibTableColumn
ruijieSystemFanPad1Speed9 = _RuijieSystemFanPad1Speed9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 55, 1, 11),
    _RuijieSystemFanPad1Speed9_Type()
)
ruijieSystemFanPad1Speed9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad1Speed9.setStatus("current")
_RuijieSystemFanPad2SpeedTable_Object = MibTable
ruijieSystemFanPad2SpeedTable = _RuijieSystemFanPad2SpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56)
)
if mibBuilder.loadTexts:
    ruijieSystemFanPad2SpeedTable.setStatus("current")
_RuijieSystemFanPad2SpeedEntry_Object = MibTableRow
ruijieSystemFanPad2SpeedEntry = _RuijieSystemFanPad2SpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56, 1)
)
ruijieSystemFanPad2SpeedEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemOamFanPad2Index"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanPad2SpeedEntry.setStatus("current")
_RuijieSystemOamFanPad2Index_Type = Integer32
_RuijieSystemOamFanPad2Index_Object = MibTableColumn
ruijieSystemOamFanPad2Index = _RuijieSystemOamFanPad2Index_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56, 1, 1),
    _RuijieSystemOamFanPad2Index_Type()
)
ruijieSystemOamFanPad2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemOamFanPad2Index.setStatus("current")
_RuijieSystemOamFanPad2Name_Type = DisplayString
_RuijieSystemOamFanPad2Name_Object = MibTableColumn
ruijieSystemOamFanPad2Name = _RuijieSystemOamFanPad2Name_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56, 1, 2),
    _RuijieSystemOamFanPad2Name_Type()
)
ruijieSystemOamFanPad2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemOamFanPad2Name.setStatus("current")
_RuijieSystemFanPad2Speed1_Type = Integer32
_RuijieSystemFanPad2Speed1_Object = MibTableColumn
ruijieSystemFanPad2Speed1 = _RuijieSystemFanPad2Speed1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56, 1, 3),
    _RuijieSystemFanPad2Speed1_Type()
)
ruijieSystemFanPad2Speed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad2Speed1.setStatus("current")
_RuijieSystemFanPad2Speed2_Type = Integer32
_RuijieSystemFanPad2Speed2_Object = MibTableColumn
ruijieSystemFanPad2Speed2 = _RuijieSystemFanPad2Speed2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56, 1, 4),
    _RuijieSystemFanPad2Speed2_Type()
)
ruijieSystemFanPad2Speed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad2Speed2.setStatus("current")
_RuijieSystemFanPad2Speed3_Type = Integer32
_RuijieSystemFanPad2Speed3_Object = MibTableColumn
ruijieSystemFanPad2Speed3 = _RuijieSystemFanPad2Speed3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 56, 1, 5),
    _RuijieSystemFanPad2Speed3_Type()
)
ruijieSystemFanPad2Speed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad2Speed3.setStatus("current")
_RuijieSystemFanPad3SpeedTable_Object = MibTable
ruijieSystemFanPad3SpeedTable = _RuijieSystemFanPad3SpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57)
)
if mibBuilder.loadTexts:
    ruijieSystemFanPad3SpeedTable.setStatus("current")
_RuijieSystemFanPad3SpeedEntry_Object = MibTableRow
ruijieSystemFanPad3SpeedEntry = _RuijieSystemFanPad3SpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1)
)
ruijieSystemFanPad3SpeedEntry.setIndexNames(
    (0, "RUIJIE-SYSTEM-MIB", "ruijieSystemOamFanPad3Index"),
)
if mibBuilder.loadTexts:
    ruijieSystemFanPad3SpeedEntry.setStatus("current")
_RuijieSystemOamFanPad3Index_Type = Integer32
_RuijieSystemOamFanPad3Index_Object = MibTableColumn
ruijieSystemOamFanPad3Index = _RuijieSystemOamFanPad3Index_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 1),
    _RuijieSystemOamFanPad3Index_Type()
)
ruijieSystemOamFanPad3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemOamFanPad3Index.setStatus("current")
_RuijieSystemOamFanPad3Name_Type = DisplayString
_RuijieSystemOamFanPad3Name_Object = MibTableColumn
ruijieSystemOamFanPad3Name = _RuijieSystemOamFanPad3Name_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 2),
    _RuijieSystemOamFanPad3Name_Type()
)
ruijieSystemOamFanPad3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemOamFanPad3Name.setStatus("current")
_RuijieSystemFanPad3Speed1_Type = Integer32
_RuijieSystemFanPad3Speed1_Object = MibTableColumn
ruijieSystemFanPad3Speed1 = _RuijieSystemFanPad3Speed1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 3),
    _RuijieSystemFanPad3Speed1_Type()
)
ruijieSystemFanPad3Speed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad3Speed1.setStatus("current")
_RuijieSystemFanPad3Speed2_Type = Integer32
_RuijieSystemFanPad3Speed2_Object = MibTableColumn
ruijieSystemFanPad3Speed2 = _RuijieSystemFanPad3Speed2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 4),
    _RuijieSystemFanPad3Speed2_Type()
)
ruijieSystemFanPad3Speed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad3Speed2.setStatus("current")
_RuijieSystemFanPad3Speed3_Type = Integer32
_RuijieSystemFanPad3Speed3_Object = MibTableColumn
ruijieSystemFanPad3Speed3 = _RuijieSystemFanPad3Speed3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 5),
    _RuijieSystemFanPad3Speed3_Type()
)
ruijieSystemFanPad3Speed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad3Speed3.setStatus("current")
_RuijieSystemFanPad3Speed4_Type = Integer32
_RuijieSystemFanPad3Speed4_Object = MibTableColumn
ruijieSystemFanPad3Speed4 = _RuijieSystemFanPad3Speed4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 6),
    _RuijieSystemFanPad3Speed4_Type()
)
ruijieSystemFanPad3Speed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad3Speed4.setStatus("current")
_RuijieSystemFanPad3Speed5_Type = Integer32
_RuijieSystemFanPad3Speed5_Object = MibTableColumn
ruijieSystemFanPad3Speed5 = _RuijieSystemFanPad3Speed5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 57, 1, 7),
    _RuijieSystemFanPad3Speed5_Type()
)
ruijieSystemFanPad3Speed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemFanPad3Speed5.setStatus("current")
_RuijieSystemParamSaveErrIdx_Type = Integer32
_RuijieSystemParamSaveErrIdx_Object = MibScalar
ruijieSystemParamSaveErrIdx = _RuijieSystemParamSaveErrIdx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 58),
    _RuijieSystemParamSaveErrIdx_Type()
)
ruijieSystemParamSaveErrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemParamSaveErrIdx.setStatus("current")


class _RuijieSystemParamSaveErrMsg_Type(DisplayString):
    """Custom type ruijieSystemParamSaveErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieSystemParamSaveErrMsg_Type.__name__ = "DisplayString"
_RuijieSystemParamSaveErrMsg_Object = MibScalar
ruijieSystemParamSaveErrMsg = _RuijieSystemParamSaveErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 59),
    _RuijieSystemParamSaveErrMsg_Type()
)
ruijieSystemParamSaveErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemParamSaveErrMsg.setStatus("current")


class _RuijieSystemDeviceLevel_Type(Integer32):
    """Custom type ruijieSystemDeviceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("core", 1),
          ("collect", 2),
          ("access", 3))
    )


_RuijieSystemDeviceLevel_Type.__name__ = "Integer32"
_RuijieSystemDeviceLevel_Object = MibScalar
ruijieSystemDeviceLevel = _RuijieSystemDeviceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 1, 60),
    _RuijieSystemDeviceLevel_Type()
)
ruijieSystemDeviceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSystemDeviceLevel.setStatus("current")
_RuijieSystemMIBTraps_ObjectIdentity = ObjectIdentity
ruijieSystemMIBTraps = _RuijieSystemMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2)
)
_RuijieSystemHardChangeDesc_Type = DisplayString
_RuijieSystemHardChangeDesc_Object = MibScalar
ruijieSystemHardChangeDesc = _RuijieSystemHardChangeDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 1),
    _RuijieSystemHardChangeDesc_Type()
)
ruijieSystemHardChangeDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieSystemHardChangeDesc.setStatus("current")
_RuijieSystemMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSystemMIBConformance = _RuijieSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 3)
)
_RuijieSystemMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSystemMIBCompliances = _RuijieSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 3, 1)
)
_RuijieSystemMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSystemMIBGroups = _RuijieSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 3, 2)
)

# Managed Objects groups

ruijieSystemMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 3, 2, 1)
)
ruijieSystemMIBGroup.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemHwVersion"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemSwVersion"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemBootVersion"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemSysCtrlVersion"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemParametersSave"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemReset"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemOutBandRate"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSwitchLayer"))
)
if mibBuilder.loadTexts:
    ruijieSystemMIBGroup.setStatus("current")


# Notification objects

ruijieSystemHardChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 2)
)
ruijieSystemHardChangeDetected.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemHardChangeDesc")
)
if mibBuilder.loadTexts:
    ruijieSystemHardChangeDetected.setStatus(
        "current"
    )

ruijieSystemPowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 3)
)
ruijieSystemPowerStateChange.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemHwPower")
)
if mibBuilder.loadTexts:
    ruijieSystemPowerStateChange.setStatus(
        "current"
    )

ruijieSystemFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 4)
)
ruijieSystemFanStateChange.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemHwFan")
)
if mibBuilder.loadTexts:
    ruijieSystemFanStateChange.setStatus(
        "current"
    )

ruijieSystemCPUusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 5)
)
ruijieSystemCPUusageTooHighTrap.setObjects(
    ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization1Min")
)
if mibBuilder.loadTexts:
    ruijieSystemCPUusageTooHighTrap.setStatus(
        "current"
    )

ruijieSystemCPUusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 6)
)
ruijieSystemCPUusageTooHighRecovTrap.setObjects(
    ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization1Min")
)
if mibBuilder.loadTexts:
    ruijieSystemCPUusageTooHighRecovTrap.setStatus(
        "current"
    )

ruijieSystemTmpTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 7)
)
ruijieSystemTmpTooHighTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    ruijieSystemTmpTooHighTrap.setStatus(
        "current"
    )

ruijieSystemTmpTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 8)
)
ruijieSystemTmpTooHighRecovTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    ruijieSystemTmpTooHighRecovTrap.setStatus(
        "current"
    )

ruijieSystemMemusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 9)
)
ruijieSystemMemusageTooHighTrap.setObjects(
    ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolCurrentUtilization")
)
if mibBuilder.loadTexts:
    ruijieSystemMemusageTooHighTrap.setStatus(
        "current"
    )

ruijieSystemMemusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 10)
)
ruijieSystemMemusageTooHighRecovTrap.setObjects(
    ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolCurrentUtilization")
)
if mibBuilder.loadTexts:
    ruijieSystemMemusageTooHighRecovTrap.setStatus(
        "current"
    )

ruijieSystemLankApCPUusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 11)
)
ruijieSystemLankApCPUusageTooHighTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization1Min"))
)
if mibBuilder.loadTexts:
    ruijieSystemLankApCPUusageTooHighTrap.setStatus(
        "current"
    )

ruijieSystemLankApCPUusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 12)
)
ruijieSystemLankApCPUusageTooHighRecovTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization1Min"))
)
if mibBuilder.loadTexts:
    ruijieSystemLankApCPUusageTooHighRecovTrap.setStatus(
        "current"
    )

ruijieSystemLankApMemusageTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 13)
)
ruijieSystemLankApMemusageTooHighTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolCurrentUtilization"))
)
if mibBuilder.loadTexts:
    ruijieSystemLankApMemusageTooHighTrap.setStatus(
        "current"
    )

ruijieSystemLankApMemusageTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 14)
)
ruijieSystemLankApMemusageTooHighRecovTrap.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolCurrentUtilization"))
)
if mibBuilder.loadTexts:
    ruijieSystemLankApMemusageTooHighRecovTrap.setStatus(
        "current"
    )

ruijieSystemResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    ruijieSystemResetTrap.setStatus(
        "current"
    )

ruijieSystemLankApResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 16)
)
ruijieSystemLankApResetTrap.setObjects(
    ("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr")
)
if mibBuilder.loadTexts:
    ruijieSystemLankApResetTrap.setStatus(
        "current"
    )

ruijieSystemPowerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 17)
)
ruijieSystemPowerOnTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemPowerIndex")
)
if mibBuilder.loadTexts:
    ruijieSystemPowerOnTrap.setStatus(
        "current"
    )

ruijieSystemPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 18)
)
ruijieSystemPowerOffTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemPowerIndex")
)
if mibBuilder.loadTexts:
    ruijieSystemPowerOffTrap.setStatus(
        "current"
    )

ruijieSystemPowerOnTrapInVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 19)
)
ruijieSystemPowerOnTrapInVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemPowerIndex"))
)
if mibBuilder.loadTexts:
    ruijieSystemPowerOnTrapInVSU.setStatus(
        "current"
    )

ruijieSystemPowerOffTrapInVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 20)
)
ruijieSystemPowerOffTrapInVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemPowerIndex"))
)
if mibBuilder.loadTexts:
    ruijieSystemPowerOffTrapInVSU.setStatus(
        "current"
    )

ruijieSystemTmpTableTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 21)
)
ruijieSystemTmpTableTooHighTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureSlotIndex")
)
if mibBuilder.loadTexts:
    ruijieSystemTmpTableTooHighTrap.setStatus(
        "current"
    )

ruijieSystemTmpTableTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 22)
)
ruijieSystemTmpTableTooHighRecovTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureSlotIndex")
)
if mibBuilder.loadTexts:
    ruijieSystemTmpTableTooHighRecovTrap.setStatus(
        "current"
    )

ruijieSystemTmpTableTooHighTrapVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 23)
)
ruijieSystemTmpTableTooHighTrapVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureDeviceIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureSlotIndex"))
)
if mibBuilder.loadTexts:
    ruijieSystemTmpTableTooHighTrapVSU.setStatus(
        "current"
    )

ruijieSystemTmpTableTooHighRecovTrapVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 24)
)
ruijieSystemTmpTableTooHighRecovTrapVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureDeviceIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemMultipleTemperatureSlotIndex"))
)
if mibBuilder.loadTexts:
    ruijieSystemTmpTableTooHighRecovTrapVSU.setStatus(
        "current"
    )

ruijieSystemFanTableStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 25)
)
ruijieSystemFanTableStateChange.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatus"))
)
if mibBuilder.loadTexts:
    ruijieSystemFanTableStateChange.setStatus(
        "current"
    )

ruijieSystemFanTableStateChangeVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 26)
)
ruijieSystemFanTableStateChangeVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusDeviceIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatus"))
)
if mibBuilder.loadTexts:
    ruijieSystemFanTableStateChangeVSU.setStatus(
        "current"
    )

ruijieSystemParamSaveErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 27)
)
ruijieSystemParamSaveErr.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemParamSaveErrIdx"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemParamSaveErrMsg"))
)
if mibBuilder.loadTexts:
    ruijieSystemParamSaveErr.setStatus(
        "current"
    )

ruijieSystemFanTableOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 28)
)
ruijieSystemFanTableOn.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatus"))
)
if mibBuilder.loadTexts:
    ruijieSystemFanTableOn.setStatus(
        "current"
    )

ruijieSystemFanTableOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 29)
)
ruijieSystemFanTableOff.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatus"))
)
if mibBuilder.loadTexts:
    ruijieSystemFanTableOff.setStatus(
        "current"
    )

ruijieSystemFanTableOnVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 30)
)
ruijieSystemFanTableOnVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusDeviceIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatus"))
)
if mibBuilder.loadTexts:
    ruijieSystemFanTableOnVSU.setStatus(
        "current"
    )

ruijieSystemFanTableOffVSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 31)
)
ruijieSystemFanTableOffVSU.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusDeviceIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusFanIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatusIndex"),
        ("RUIJIE-SYSTEM-MIB", "ruijieSystemFanStatus"))
)
if mibBuilder.loadTexts:
    ruijieSystemFanTableOffVSU.setStatus(
        "current"
    )

ruijieSwitchOverNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 32)
)
ruijieSwitchOverNotify.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID")
)
if mibBuilder.loadTexts:
    ruijieSwitchOverNotify.setStatus(
        "current"
    )

ruijieResetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 33)
)
ruijieResetNotify.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ruijieResetNotify.setStatus(
        "current"
    )

ruijieOfflineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 34)
)
ruijieOfflineNotify.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ruijieOfflineNotify.setStatus(
        "current"
    )

ruijieSystemPowerOnNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 35)
)
ruijieSystemPowerOnNotify.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ruijieSystemPowerOnNotify.setStatus(
        "current"
    )

ruijieSystemPowerOffNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 36)
)
ruijieSystemPowerOffNotify.setObjects(
      *(("RUIJIE-SYSTEM-MIB", "ruijieSystemSwitchID"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ruijieSystemPowerOffNotify.setStatus(
        "current"
    )

ruijieSystemMemusageTooHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 37)
)
ruijieSystemMemusageTooHighAlarm.setObjects(
      *(("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolName"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolCurrentUtilization"))
)
if mibBuilder.loadTexts:
    ruijieSystemMemusageTooHighAlarm.setStatus(
        "current"
    )

ruijieSystemMemusageTooHighRecovAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 38)
)
ruijieSystemMemusageTooHighRecovAlarm.setObjects(
      *(("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolName"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolCurrentUtilization"))
)
if mibBuilder.loadTexts:
    ruijieSystemMemusageTooHighRecovAlarm.setStatus(
        "current"
    )

ruijieSystemCPUusageTooHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 39)
)
ruijieSystemCPUusageTooHighAlarm.setObjects(
      *(("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalName"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotal1min"))
)
if mibBuilder.loadTexts:
    ruijieSystemCPUusageTooHighAlarm.setStatus(
        "current"
    )

ruijieSystemCPUusageTooHighRecovAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 2, 40)
)
ruijieSystemCPUusageTooHighRecovAlarm.setObjects(
      *(("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalName"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotal1min"))
)
if mibBuilder.loadTexts:
    ruijieSystemCPUusageTooHighRecovAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 1, 3, 1, 1)
)
ruijieSystemMIBCompliance.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieSystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SYSTEM-MIB",
    **{"ruijieSystemMIB": ruijieSystemMIB,
       "ruijieSystemMIBObjects": ruijieSystemMIBObjects,
       "ruijieSystemHwVersion": ruijieSystemHwVersion,
       "ruijieSystemSwVersion": ruijieSystemSwVersion,
       "ruijieSystemBootVersion": ruijieSystemBootVersion,
       "ruijieSystemSysCtrlVersion": ruijieSystemSysCtrlVersion,
       "ruijieSystemParametersSave": ruijieSystemParametersSave,
       "ruijieSystemOutBandRate": ruijieSystemOutBandRate,
       "ruijieSystemReset": ruijieSystemReset,
       "ruijieSwitchLayer": ruijieSwitchLayer,
       "ruijieSystemHwPower": ruijieSystemHwPower,
       "ruijieSystemHwFan": ruijieSystemHwFan,
       "ruijieSystemOutBandTimeout": ruijieSystemOutBandTimeout,
       "ruijieSystemTelnetTimeout": ruijieSystemTelnetTimeout,
       "ruijieSystemMainFile": ruijieSystemMainFile,
       "ruijieSystemCurrentPower": ruijieSystemCurrentPower,
       "ruijieSystemRemainPower": ruijieSystemRemainPower,
       "ruijieSystemTemperature": ruijieSystemTemperature,
       "ruijieSystemElectricalSourceNum": ruijieSystemElectricalSourceNum,
       "ruijieSystemElectricalSourceIsNormalTable": ruijieSystemElectricalSourceIsNormalTable,
       "ruijieSystemElectricalSourceIsNormalEntry": ruijieSystemElectricalSourceIsNormalEntry,
       "ruijieSystemElectricalSourceIsNormalIndex": ruijieSystemElectricalSourceIsNormalIndex,
       "ruijieSystemElectricalSourceIsNormal": ruijieSystemElectricalSourceIsNormal,
       "ruijieSystemElectricalSourceName": ruijieSystemElectricalSourceName,
       "ruijieSystemCurrentVoltage": ruijieSystemCurrentVoltage,
       "ruijieSystemFanNUM": ruijieSystemFanNUM,
       "ruijieSystemFanIsNormalTable": ruijieSystemFanIsNormalTable,
       "ruijieSystemFanIsNormalEntry": ruijieSystemFanIsNormalEntry,
       "ruijieSystemFanIsNormalIndex": ruijieSystemFanIsNormalIndex,
       "ruijieSystemFanIsNormal": ruijieSystemFanIsNormal,
       "ruijieSystemFanName": ruijieSystemFanName,
       "ruijieSystemFanSpeed": ruijieSystemFanSpeed,
       "ruijieSystemReloadTimeRemain": ruijieSystemReloadTimeRemain,
       "ruijieSystemTemperatureTable": ruijieSystemTemperatureTable,
       "ruijieSystemTemperatureEntry": ruijieSystemTemperatureEntry,
       "ruijieSystemTemperatureIndex": ruijieSystemTemperatureIndex,
       "ruijieSystemTemperatureName": ruijieSystemTemperatureName,
       "ruijieSystemTemperatureCurrent": ruijieSystemTemperatureCurrent,
       "ruijieSystemTemperatureWarningVaule": ruijieSystemTemperatureWarningVaule,
       "ruijieSystemTemperatureCritialVaule": ruijieSystemTemperatureCritialVaule,
       "ruijieSystemSerialno": ruijieSystemSerialno,
       "ruijieSystemVersionTable": ruijieSystemVersionTable,
       "ruijieSystemVersionEntry": ruijieSystemVersionEntry,
       "ruijieSystemVersionIndex": ruijieSystemVersionIndex,
       "ruijieSystemVersionName": ruijieSystemVersionName,
       "ruijieSystemVersionSwBoot": ruijieSystemVersionSwBoot,
       "ruijieSystemVersionSwCtrl": ruijieSystemVersionSwCtrl,
       "ruijieSystemVersionSwMain": ruijieSystemVersionSwMain,
       "ruijieSystemVersionHw": ruijieSystemVersionHw,
       "ruijieSystemVersionSerialno": ruijieSystemVersionSerialno,
       "ruijieSystemSysModel": ruijieSystemSysModel,
       "ruijieSystemUptime": ruijieSystemUptime,
       "ruijieSystemSampleTime": ruijieSystemSampleTime,
       "ruijieSystemStatWindowTime": ruijieSystemStatWindowTime,
       "ruijieSystemManufacturer": ruijieSystemManufacturer,
       "ruijieSystemCurrentTime": ruijieSystemCurrentTime,
       "ruijieSystemWarnResendTime": ruijieSystemWarnResendTime,
       "ruijieSystemSoftwareName": ruijieSystemSoftwareName,
       "ruijieSystemSoftwareManufacturer": ruijieSystemSoftwareManufacturer,
       "ruijieSystemCpuType": ruijieSystemCpuType,
       "ruijieSystemMemoryType": ruijieSystemMemoryType,
       "ruijieSystemMemorySize": ruijieSystemMemorySize,
       "ruijieSystemFlashSize": ruijieSystemFlashSize,
       "ruijieSystemLankApTable": ruijieSystemLankApTable,
       "ruijieSystemLankApEntry": ruijieSystemLankApEntry,
       "ruijieSystemLankApMacAddr": ruijieSystemLankApMacAddr,
       "ruijieSystemLankApStatWindowTime": ruijieSystemLankApStatWindowTime,
       "ruijieSystemLankApSampleTime": ruijieSystemLankApSampleTime,
       "ruijieSystemLankApReset": ruijieSystemLankApReset,
       "ruijieSystemLankApSoftwareName": ruijieSystemLankApSoftwareName,
       "ruijieSystemLankApSwVersion": ruijieSystemLankApSwVersion,
       "ruijieSystemLankApSoftwareManufacturer": ruijieSystemLankApSoftwareManufacturer,
       "ruijieSystemLankApCpuType": ruijieSystemLankApCpuType,
       "ruijieSystemLankApMemoryType": ruijieSystemLankApMemoryType,
       "ruijieSystemLankApMemorySize": ruijieSystemLankApMemorySize,
       "ruijieSystemLankAPFlashSize": ruijieSystemLankAPFlashSize,
       "ruijieSystemLankApManufacturer": ruijieSystemLankApManufacturer,
       "ruijieSystemLankApSerialno": ruijieSystemLankApSerialno,
       "ruijieSystemLankApSysModel": ruijieSystemLankApSysModel,
       "ruijieSystemLankApUptime": ruijieSystemLankApUptime,
       "ruijieSystemLankApAccurateUptime": ruijieSystemLankApAccurateUptime,
       "ruijieSystemLankApHwVersion": ruijieSystemLankApHwVersion,
       "ruijieSystemBoardTemperatureTable": ruijieSystemBoardTemperatureTable,
       "ruijieSystemBoardTemperatureEntry": ruijieSystemBoardTemperatureEntry,
       "ruijieSystemBoardTemperatureIndex": ruijieSystemBoardTemperatureIndex,
       "ruijieSystemBoardTemperatureName": ruijieSystemBoardTemperatureName,
       "ruijieSystemBoardTemperatureCurrent": ruijieSystemBoardTemperatureCurrent,
       "ruijieSystemElectricalInformationTable": ruijieSystemElectricalInformationTable,
       "ruijieSystemElectricalInformationEntry": ruijieSystemElectricalInformationEntry,
       "ruijieSystemElectricalInformationDeviceIndex": ruijieSystemElectricalInformationDeviceIndex,
       "ruijieSystemElectricalInformationIndex": ruijieSystemElectricalInformationIndex,
       "ruijieSystemElectricalInformationStatus": ruijieSystemElectricalInformationStatus,
       "ruijieSystemElectricalInformationType": ruijieSystemElectricalInformationType,
       "ruijieSystemElectricalInformationAttribute": ruijieSystemElectricalInformationAttribute,
       "ruijieSystemElectricalInformationSofeVersion": ruijieSystemElectricalInformationSofeVersion,
       "ruijieSystemElectricalInformationHardwareVersion": ruijieSystemElectricalInformationHardwareVersion,
       "ruijieSystemElectricalInformationSerial": ruijieSystemElectricalInformationSerial,
       "ruijieSystemElectricalInformationProductionDate": ruijieSystemElectricalInformationProductionDate,
       "ruijieSystemElectricalInformationRatedPower": ruijieSystemElectricalInformationRatedPower,
       "ruijieSystemElectricalInformationInVoltage": ruijieSystemElectricalInformationInVoltage,
       "ruijieSystemElectricalInformationInCurrent": ruijieSystemElectricalInformationInCurrent,
       "ruijieSystemElectricalInformationOutVoltage": ruijieSystemElectricalInformationOutVoltage,
       "ruijieSystemElectricalInformationOutCurrent": ruijieSystemElectricalInformationOutCurrent,
       "ruijieSystemElectricalInformationOutPower": ruijieSystemElectricalInformationOutPower,
       "ruijieSystemElectricalInformationTemperature": ruijieSystemElectricalInformationTemperature,
       "ruijieSystemElectricalInformationAirflowCoexist": ruijieSystemElectricalInformationAirflowCoexist,
       "ruijieSystemElectricalInformationWarningStatus": ruijieSystemElectricalInformationWarningStatus,
       "ruijieSystemFanInformationTable": ruijieSystemFanInformationTable,
       "ruijieSystemFanInformationEntry": ruijieSystemFanInformationEntry,
       "ruijieSystemFanInformationDeviceIndex": ruijieSystemFanInformationDeviceIndex,
       "ruijieSystemFanInformationFanIndex": ruijieSystemFanInformationFanIndex,
       "ruijieSystemFanInformationStatus": ruijieSystemFanInformationStatus,
       "ruijieSystemFanInformationType": ruijieSystemFanInformationType,
       "ruijieSystemFanInformationAttribute": ruijieSystemFanInformationAttribute,
       "ruijieSystemFanInformationSofeVersion": ruijieSystemFanInformationSofeVersion,
       "ruijieSystemFanInformationFirmwareVersion": ruijieSystemFanInformationFirmwareVersion,
       "ruijieSystemFanInformationHardwareVersion": ruijieSystemFanInformationHardwareVersion,
       "ruijieSystemFanInformationSerial": ruijieSystemFanInformationSerial,
       "ruijieSystemFanInformationProductionDate": ruijieSystemFanInformationProductionDate,
       "ruijieSystemFanInformationTemperature": ruijieSystemFanInformationTemperature,
       "ruijieSystemFanInformationNumber": ruijieSystemFanInformationNumber,
       "ruijieSystemFanInformationAirflowCoexist": ruijieSystemFanInformationAirflowCoexist,
       "ruijieSystemFanInformationWarningStatus": ruijieSystemFanInformationWarningStatus,
       "ruijieSystemFanStatusTable": ruijieSystemFanStatusTable,
       "ruijieSystemFanStatusEntry": ruijieSystemFanStatusEntry,
       "ruijieSystemFanStatusDeviceIndex": ruijieSystemFanStatusDeviceIndex,
       "ruijieSystemFanStatusFanIndex": ruijieSystemFanStatusFanIndex,
       "ruijieSystemFanStatusIndex": ruijieSystemFanStatusIndex,
       "ruijieSystemFanStatus": ruijieSystemFanStatus,
       "ruijieSystemFanStatusLevel": ruijieSystemFanStatusLevel,
       "ruijieSystemFanStatusSpeed": ruijieSystemFanStatusSpeed,
       "ruijieSystemMultipleTemperatureTable": ruijieSystemMultipleTemperatureTable,
       "ruijieSystemMultipleTemperatureEntry": ruijieSystemMultipleTemperatureEntry,
       "ruijieSystemMultipleTemperatureDeviceIndex": ruijieSystemMultipleTemperatureDeviceIndex,
       "ruijieSystemMultipleTemperatureSlotIndex": ruijieSystemMultipleTemperatureSlotIndex,
       "ruijieSystemMultipleTemperatureIndex": ruijieSystemMultipleTemperatureIndex,
       "ruijieSystemMultipleTemperatureName": ruijieSystemMultipleTemperatureName,
       "ruijieSystemMultipleTemperatureCurrent": ruijieSystemMultipleTemperatureCurrent,
       "ruijieSystemMultipleTemperatureWarning": ruijieSystemMultipleTemperatureWarning,
       "ruijieSystemMultipleTemperatureCritical": ruijieSystemMultipleTemperatureCritical,
       "ruijieSystemAccurateUptime": ruijieSystemAccurateUptime,
       "ruijieSystemPowerIndex": ruijieSystemPowerIndex,
       "ruijieSystemSwitchID": ruijieSystemSwitchID,
       "ruijieSystemApDeviceDescriptionTable": ruijieSystemApDeviceDescriptionTable,
       "ruijieSystemApDeviceDescriptionEntry": ruijieSystemApDeviceDescriptionEntry,
       "ruijieSystemApDescMacAddr": ruijieSystemApDescMacAddr,
       "ruijieSystemApMemoryType": ruijieSystemApMemoryType,
       "ruijieSystemApMemorySize": ruijieSystemApMemorySize,
       "ruijieSystemAPFlashType": ruijieSystemAPFlashType,
       "ruijieSystemAPFlashSize": ruijieSystemAPFlashSize,
       "ruijieSystemApNVRAMSize": ruijieSystemApNVRAMSize,
       "ruijieSystemApCFSize": ruijieSystemApCFSize,
       "ruijieSystemApCPUType": ruijieSystemApCPUType,
       "ruijieSystemApDeviceStatisticsTable": ruijieSystemApDeviceStatisticsTable,
       "ruijieSystemApDeviceStatisticsEntry": ruijieSystemApDeviceStatisticsEntry,
       "ruijieSystemApStatMacAddr": ruijieSystemApStatMacAddr,
       "ruijieSystemApInterfaceNum": ruijieSystemApInterfaceNum,
       "ruijieSystemApUptime": ruijieSystemApUptime,
       "ruijieSystemApCPUUtilizationCurrent": ruijieSystemApCPUUtilizationCurrent,
       "ruijieSystemApCPUUtilizationAverage": ruijieSystemApCPUUtilizationAverage,
       "ruijieSystemApMemoryPoolCurrentUtilization": ruijieSystemApMemoryPoolCurrentUtilization,
       "ruijieSystemApMemoryPoolAverageUtilization": ruijieSystemApMemoryPoolAverageUtilization,
       "ruijieSystemApFlashFreeSize": ruijieSystemApFlashFreeSize,
       "ruijieSystemAPDeviceTemperature": ruijieSystemAPDeviceTemperature,
       "ruijieSystemUptimeMsLow": ruijieSystemUptimeMsLow,
       "ruijieSystemUptimeMsHigh": ruijieSystemUptimeMsHigh,
       "ruijieSystemFanSNTable": ruijieSystemFanSNTable,
       "ruijieSystemFanSNEntry": ruijieSystemFanSNEntry,
       "ruijieSystemFanPadIndex": ruijieSystemFanPadIndex,
       "ruijieSystemFanPadName": ruijieSystemFanPadName,
       "ruijieSystemFanPadSN": ruijieSystemFanPadSN,
       "ruijieSystemDsfSNTable": ruijieSystemDsfSNTable,
       "ruijieSystemDsfSNEntry": ruijieSystemDsfSNEntry,
       "ruijieSystemDsfIndex": ruijieSystemDsfIndex,
       "ruijieSystemDsfName": ruijieSystemDsfName,
       "ruijieSystemDsfSN": ruijieSystemDsfSN,
       "ruijieSystemPowerSNTable": ruijieSystemPowerSNTable,
       "ruijieSystemPowerSNEntry": ruijieSystemPowerSNEntry,
       "ruijieSystemPowerSNIndex": ruijieSystemPowerSNIndex,
       "ruijieSystemPowerSNName": ruijieSystemPowerSNName,
       "ruijieSystemPowerSN": ruijieSystemPowerSN,
       "ruijieSystemFanPad1SpeedTable": ruijieSystemFanPad1SpeedTable,
       "ruijieSystemFanPad1SpeedEntry": ruijieSystemFanPad1SpeedEntry,
       "ruijieSystemOamFanPad1Index": ruijieSystemOamFanPad1Index,
       "ruijieSystemOamFanPad1Name": ruijieSystemOamFanPad1Name,
       "ruijieSystemFanPad1Speed1": ruijieSystemFanPad1Speed1,
       "ruijieSystemFanPad1Speed2": ruijieSystemFanPad1Speed2,
       "ruijieSystemFanPad1Speed3": ruijieSystemFanPad1Speed3,
       "ruijieSystemFanPad1Speed4": ruijieSystemFanPad1Speed4,
       "ruijieSystemFanPad1Speed5": ruijieSystemFanPad1Speed5,
       "ruijieSystemFanPad1Speed6": ruijieSystemFanPad1Speed6,
       "ruijieSystemFanPad1Speed7": ruijieSystemFanPad1Speed7,
       "ruijieSystemFanPad1Speed8": ruijieSystemFanPad1Speed8,
       "ruijieSystemFanPad1Speed9": ruijieSystemFanPad1Speed9,
       "ruijieSystemFanPad2SpeedTable": ruijieSystemFanPad2SpeedTable,
       "ruijieSystemFanPad2SpeedEntry": ruijieSystemFanPad2SpeedEntry,
       "ruijieSystemOamFanPad2Index": ruijieSystemOamFanPad2Index,
       "ruijieSystemOamFanPad2Name": ruijieSystemOamFanPad2Name,
       "ruijieSystemFanPad2Speed1": ruijieSystemFanPad2Speed1,
       "ruijieSystemFanPad2Speed2": ruijieSystemFanPad2Speed2,
       "ruijieSystemFanPad2Speed3": ruijieSystemFanPad2Speed3,
       "ruijieSystemFanPad3SpeedTable": ruijieSystemFanPad3SpeedTable,
       "ruijieSystemFanPad3SpeedEntry": ruijieSystemFanPad3SpeedEntry,
       "ruijieSystemOamFanPad3Index": ruijieSystemOamFanPad3Index,
       "ruijieSystemOamFanPad3Name": ruijieSystemOamFanPad3Name,
       "ruijieSystemFanPad3Speed1": ruijieSystemFanPad3Speed1,
       "ruijieSystemFanPad3Speed2": ruijieSystemFanPad3Speed2,
       "ruijieSystemFanPad3Speed3": ruijieSystemFanPad3Speed3,
       "ruijieSystemFanPad3Speed4": ruijieSystemFanPad3Speed4,
       "ruijieSystemFanPad3Speed5": ruijieSystemFanPad3Speed5,
       "ruijieSystemParamSaveErrIdx": ruijieSystemParamSaveErrIdx,
       "ruijieSystemParamSaveErrMsg": ruijieSystemParamSaveErrMsg,
       "ruijieSystemDeviceLevel": ruijieSystemDeviceLevel,
       "ruijieSystemMIBTraps": ruijieSystemMIBTraps,
       "ruijieSystemHardChangeDesc": ruijieSystemHardChangeDesc,
       "ruijieSystemHardChangeDetected": ruijieSystemHardChangeDetected,
       "ruijieSystemPowerStateChange": ruijieSystemPowerStateChange,
       "ruijieSystemFanStateChange": ruijieSystemFanStateChange,
       "ruijieSystemCPUusageTooHighTrap": ruijieSystemCPUusageTooHighTrap,
       "ruijieSystemCPUusageTooHighRecovTrap": ruijieSystemCPUusageTooHighRecovTrap,
       "ruijieSystemTmpTooHighTrap": ruijieSystemTmpTooHighTrap,
       "ruijieSystemTmpTooHighRecovTrap": ruijieSystemTmpTooHighRecovTrap,
       "ruijieSystemMemusageTooHighTrap": ruijieSystemMemusageTooHighTrap,
       "ruijieSystemMemusageTooHighRecovTrap": ruijieSystemMemusageTooHighRecovTrap,
       "ruijieSystemLankApCPUusageTooHighTrap": ruijieSystemLankApCPUusageTooHighTrap,
       "ruijieSystemLankApCPUusageTooHighRecovTrap": ruijieSystemLankApCPUusageTooHighRecovTrap,
       "ruijieSystemLankApMemusageTooHighTrap": ruijieSystemLankApMemusageTooHighTrap,
       "ruijieSystemLankApMemusageTooHighRecovTrap": ruijieSystemLankApMemusageTooHighRecovTrap,
       "ruijieSystemResetTrap": ruijieSystemResetTrap,
       "ruijieSystemLankApResetTrap": ruijieSystemLankApResetTrap,
       "ruijieSystemPowerOnTrap": ruijieSystemPowerOnTrap,
       "ruijieSystemPowerOffTrap": ruijieSystemPowerOffTrap,
       "ruijieSystemPowerOnTrapInVSU": ruijieSystemPowerOnTrapInVSU,
       "ruijieSystemPowerOffTrapInVSU": ruijieSystemPowerOffTrapInVSU,
       "ruijieSystemTmpTableTooHighTrap": ruijieSystemTmpTableTooHighTrap,
       "ruijieSystemTmpTableTooHighRecovTrap": ruijieSystemTmpTableTooHighRecovTrap,
       "ruijieSystemTmpTableTooHighTrapVSU": ruijieSystemTmpTableTooHighTrapVSU,
       "ruijieSystemTmpTableTooHighRecovTrapVSU": ruijieSystemTmpTableTooHighRecovTrapVSU,
       "ruijieSystemFanTableStateChange": ruijieSystemFanTableStateChange,
       "ruijieSystemFanTableStateChangeVSU": ruijieSystemFanTableStateChangeVSU,
       "ruijieSystemParamSaveErr": ruijieSystemParamSaveErr,
       "ruijieSystemFanTableOn": ruijieSystemFanTableOn,
       "ruijieSystemFanTableOff": ruijieSystemFanTableOff,
       "ruijieSystemFanTableOnVSU": ruijieSystemFanTableOnVSU,
       "ruijieSystemFanTableOffVSU": ruijieSystemFanTableOffVSU,
       "ruijieSwitchOverNotify": ruijieSwitchOverNotify,
       "ruijieResetNotify": ruijieResetNotify,
       "ruijieOfflineNotify": ruijieOfflineNotify,
       "ruijieSystemPowerOnNotify": ruijieSystemPowerOnNotify,
       "ruijieSystemPowerOffNotify": ruijieSystemPowerOffNotify,
       "ruijieSystemMemusageTooHighAlarm": ruijieSystemMemusageTooHighAlarm,
       "ruijieSystemMemusageTooHighRecovAlarm": ruijieSystemMemusageTooHighRecovAlarm,
       "ruijieSystemCPUusageTooHighAlarm": ruijieSystemCPUusageTooHighAlarm,
       "ruijieSystemCPUusageTooHighRecovAlarm": ruijieSystemCPUusageTooHighRecovAlarm,
       "ruijieSystemMIBConformance": ruijieSystemMIBConformance,
       "ruijieSystemMIBCompliances": ruijieSystemMIBCompliances,
       "ruijieSystemMIBCompliance": ruijieSystemMIBCompliance,
       "ruijieSystemMIBGroups": ruijieSystemMIBGroups,
       "ruijieSystemMIBGroup": ruijieSystemMIBGroup}
)
