# SNMP MIB module (TROPIC-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-SHELF-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnShelfMIB,
 tnShelfModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnShelfMIB",
    "tnShelfModules")

(AluWdmWtClkValues,
 TnCommand,
 TnRackSize,
 TropicCardCLEI,
 TropicCardManufacturingPartNumber,
 TropicCardSerialNumber,
 TropicLEDColorType,
 TropicLEDStateType,
 TropicShelfIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmWtClkValues",
    "TnCommand",
    "TnRackSize",
    "TropicCardCLEI",
    "TropicCardManufacturingPartNumber",
    "TropicCardSerialNumber",
    "TropicLEDColorType",
    "TropicLEDStateType",
    "TropicShelfIndexType")


# MODULE-IDENTITY

tnShelfMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfMibModule.setRevisions(
        ("2008-02-16 12:00",
         "2008-03-06 12:00",
         "2008-04-05 12:00",
         "2008-05-29 12:00",
         "2008-06-05 12:00",
         "2009-04-27 12:00",
         "2009-05-19 12:00",
         "2009-06-07 12:00",
         "2009-07-15 12:00",
         "2009-09-09 12:00",
         "2009-09-15 12:00",
         "2009-12-11 12:00",
         "2010-06-04 12:00",
         "2010-06-28 12:00",
         "2010-09-13 12:00",
         "2010-10-04 12:00",
         "2010-10-12 12:00",
         "2010-12-16 12:00",
         "2011-02-06 12:00",
         "2011-04-07 12:00",
         "2012-02-06 12:00",
         "2012-02-23 12:00",
         "2012-03-29 12:00",
         "2012-09-06 12:00",
         "2012-09-25 12:00",
         "2012-12-14 12:00",
         "2013-04-29 12:00",
         "2013-05-21 12:00",
         "2013-08-07 12:00",
         "2013-09-06 12:00",
         "2013-11-14 12:00",
         "2013-12-15 12:00",
         "2014-02-26 12:00",
         "2014-07-25 12:00",
         "2014-09-12 12:00",
         "2015-06-04 12:00",
         "2015-07-31 12:00",
         "2015-08-06 12:00",
         "2015-08-25 12:00",
         "2015-09-30 12:00",
         "2015-10-20 12:00",
         "2015-12-07 12:00",
         "2015-12-24 12:00",
         "2016-02-01 12:00",
         "2016-05-06 12:00",
         "2016-06-03 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmExpectedAmpPF(TextualConvention, Integer32):
    status = "current"
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
        *(("amps3dot7", 1),
          ("amps4dot1", 2),
          ("amps8dot5", 3),
          ("amps20dot6", 4),
          ("ampsdc30", 5),
          ("ampsac7", 6),
          ("na", 7))
    )



# MIB Managed Objects in the order of their OIDs

_TnShelfConf_ObjectIdentity = ObjectIdentity
tnShelfConf = _TnShelfConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1)
)
_TnShelfGroups_ObjectIdentity = ObjectIdentity
tnShelfGroups = _TnShelfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1)
)
_TnShelfCompliances_ObjectIdentity = ObjectIdentity
tnShelfCompliances = _TnShelfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 2)
)
_TnShelfObjs_ObjectIdentity = ObjectIdentity
tnShelfObjs = _TnShelfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2)
)
_TnShelfBasics_ObjectIdentity = ObjectIdentity
tnShelfBasics = _TnShelfBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1)
)
_TnShelfTable_Object = MibTable
tnShelfTable = _TnShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfTable.setStatus("current")
_TnShelfEntry_Object = MibTableRow
tnShelfEntry = _TnShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1)
)
tnShelfEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfEntry.setStatus("current")
_TnShelfIndex_Type = TropicShelfIndexType
_TnShelfIndex_Object = MibTableColumn
tnShelfIndex = _TnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 1),
    _TnShelfIndex_Type()
)
tnShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnShelfIndex.setStatus("current")


class _TnShelfName_Type(SnmpAdminString):
    """Custom type tnShelfName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnShelfName_Type.__name__ = "SnmpAdminString"
_TnShelfName_Object = MibTableColumn
tnShelfName = _TnShelfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 2),
    _TnShelfName_Type()
)
tnShelfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfName.setStatus("current")


class _TnShelfDescr_Type(SnmpAdminString):
    """Custom type tnShelfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnShelfDescr_Type.__name__ = "SnmpAdminString"
_TnShelfDescr_Object = MibTableColumn
tnShelfDescr = _TnShelfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 3),
    _TnShelfDescr_Type()
)
tnShelfDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDescr.setStatus("current")
_TnShelfSerialNum_Type = Integer32
_TnShelfSerialNum_Object = MibTableColumn
tnShelfSerialNum = _TnShelfSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 4),
    _TnShelfSerialNum_Type()
)
tnShelfSerialNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfSerialNum.setStatus("current")
_TnShelfProgrammedType_Type = ObjectIdentifier
_TnShelfProgrammedType_Object = MibTableColumn
tnShelfProgrammedType = _TnShelfProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 5),
    _TnShelfProgrammedType_Type()
)
tnShelfProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfProgrammedType.setStatus("current")
_TnShelfPresentType_Type = ObjectIdentifier
_TnShelfPresentType_Object = MibTableColumn
tnShelfPresentType = _TnShelfPresentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 6),
    _TnShelfPresentType_Type()
)
tnShelfPresentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfPresentType.setStatus("current")


class _TnShelfActivitySwitch_Type(TnCommand):
    """Custom type tnShelfActivitySwitch based on TnCommand"""
    defaultValue = 1


_TnShelfActivitySwitch_Type.__name__ = "TnCommand"
_TnShelfActivitySwitch_Object = MibTableColumn
tnShelfActivitySwitch = _TnShelfActivitySwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 7),
    _TnShelfActivitySwitch_Type()
)
tnShelfActivitySwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfActivitySwitch.setStatus("current")


class _TnShelfLampTest_Type(TnCommand):
    """Custom type tnShelfLampTest based on TnCommand"""
    defaultValue = 1


_TnShelfLampTest_Type.__name__ = "TnCommand"
_TnShelfLampTest_Object = MibTableColumn
tnShelfLampTest = _TnShelfLampTest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 8),
    _TnShelfLampTest_Type()
)
tnShelfLampTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLampTest.setStatus("current")
_TnShelfMateCCReadyToProtect_Type = TruthValue
_TnShelfMateCCReadyToProtect_Object = MibTableColumn
tnShelfMateCCReadyToProtect = _TnShelfMateCCReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 9),
    _TnShelfMateCCReadyToProtect_Type()
)
tnShelfMateCCReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfMateCCReadyToProtect.setStatus("current")


class _TnShelfIsUnmanaged_Type(TruthValue):
    """Custom type tnShelfIsUnmanaged based on TruthValue"""
    defaultValue = 2


_TnShelfIsUnmanaged_Type.__name__ = "TruthValue"
_TnShelfIsUnmanaged_Object = MibTableColumn
tnShelfIsUnmanaged = _TnShelfIsUnmanaged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 10),
    _TnShelfIsUnmanaged_Type()
)
tnShelfIsUnmanaged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfIsUnmanaged.setStatus("current")


class _TnShelfExpectedAmps_Type(Integer32):
    """Custom type tnShelfExpectedAmps based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("amps30", 1),
          ("amps50", 2),
          ("amps70", 3),
          ("amps20", 4),
          ("auto", 5),
          ("amps35", 6),
          ("amps5", 7),
          ("amps7", 8),
          ("amps100", 9),
          ("amps150", 10),
          ("amps60", 11),
          ("amps275", 12),
          ("amps2x50", 13),
          ("amps2x60", 14),
          ("amps3x60", 15),
          ("amps20dot6", 16),
          ("amps8dot5", 17),
          ("amps3dot7", 18),
          ("ampsMix", 19),
          ("amps4dot1", 20),
          ("ampsNa", 21),
          ("amps3x50", 22),
          ("amps320", 23),
          ("amps63", 24))
    )


_TnShelfExpectedAmps_Type.__name__ = "Integer32"
_TnShelfExpectedAmps_Object = MibTableColumn
tnShelfExpectedAmps = _TnShelfExpectedAmps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 11),
    _TnShelfExpectedAmps_Type()
)
tnShelfExpectedAmps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedAmps.setStatus("current")


class _TnShelfSerialNumber_Type(SnmpAdminString):
    """Custom type tnShelfSerialNumber based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnShelfSerialNumber_Type.__name__ = "SnmpAdminString"
_TnShelfSerialNumber_Object = MibTableColumn
tnShelfSerialNumber = _TnShelfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 12),
    _TnShelfSerialNumber_Type()
)
tnShelfSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfSerialNumber.setStatus("current")


class _TnShelfAINS_Type(TruthValue):
    """Custom type tnShelfAINS based on TruthValue"""
    defaultValue = 2


_TnShelfAINS_Type.__name__ = "TruthValue"
_TnShelfAINS_Object = MibTableColumn
tnShelfAINS = _TnShelfAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 13),
    _TnShelfAINS_Type()
)
tnShelfAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfAINS.setStatus("current")
_TnShelfStatusLEDColor_Type = TropicLEDColorType
_TnShelfStatusLEDColor_Object = MibTableColumn
tnShelfStatusLEDColor = _TnShelfStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 15),
    _TnShelfStatusLEDColor_Type()
)
tnShelfStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfStatusLEDColor.setStatus("current")
_TnShelfStatusLEDState_Type = TropicLEDStateType
_TnShelfStatusLEDState_Object = MibTableColumn
tnShelfStatusLEDState = _TnShelfStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 16),
    _TnShelfStatusLEDState_Type()
)
tnShelfStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfStatusLEDState.setStatus("current")


class _TnShelfWTMode_Type(TruthValue):
    """Custom type tnShelfWTMode based on TruthValue"""
    defaultValue = 1


_TnShelfWTMode_Type.__name__ = "TruthValue"
_TnShelfWTMode_Object = MibTableColumn
tnShelfWTMode = _TnShelfWTMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 17),
    _TnShelfWTMode_Type()
)
tnShelfWTMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfWTMode.setStatus("current")


class _TnShelfActivityMt0cSwitch_Type(TnCommand):
    """Custom type tnShelfActivityMt0cSwitch based on TnCommand"""
    defaultValue = 1


_TnShelfActivityMt0cSwitch_Type.__name__ = "TnCommand"
_TnShelfActivityMt0cSwitch_Object = MibTableColumn
tnShelfActivityMt0cSwitch = _TnShelfActivityMt0cSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 18),
    _TnShelfActivityMt0cSwitch_Type()
)
tnShelfActivityMt0cSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfActivityMt0cSwitch.setStatus("current")
_TnShelfMateMt0cReadyToProtect_Type = TruthValue
_TnShelfMateMt0cReadyToProtect_Object = MibTableColumn
tnShelfMateMt0cReadyToProtect = _TnShelfMateMt0cReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 19),
    _TnShelfMateMt0cReadyToProtect_Type()
)
tnShelfMateMt0cReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfMateMt0cReadyToProtect.setStatus("current")


class _TnShelfExpectedPfa_Type(AluWdmExpectedAmpPF):
    """Custom type tnShelfExpectedPfa based on AluWdmExpectedAmpPF"""
    defaultValue = 1


_TnShelfExpectedPfa_Type.__name__ = "AluWdmExpectedAmpPF"
_TnShelfExpectedPfa_Object = MibTableColumn
tnShelfExpectedPfa = _TnShelfExpectedPfa_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 20),
    _TnShelfExpectedPfa_Type()
)
tnShelfExpectedPfa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedPfa.setStatus("current")


class _TnShelfExpectedPfb_Type(AluWdmExpectedAmpPF):
    """Custom type tnShelfExpectedPfb based on AluWdmExpectedAmpPF"""
    defaultValue = 3


_TnShelfExpectedPfb_Type.__name__ = "AluWdmExpectedAmpPF"
_TnShelfExpectedPfb_Object = MibTableColumn
tnShelfExpectedPfb = _TnShelfExpectedPfb_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 21),
    _TnShelfExpectedPfb_Type()
)
tnShelfExpectedPfb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedPfb.setStatus("current")


class _TnShelfHighVoltageThreshold_Type(Unsigned32):
    """Custom type tnShelfHighVoltageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8500),
    )


_TnShelfHighVoltageThreshold_Type.__name__ = "Unsigned32"
_TnShelfHighVoltageThreshold_Object = MibTableColumn
tnShelfHighVoltageThreshold = _TnShelfHighVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 22),
    _TnShelfHighVoltageThreshold_Type()
)
tnShelfHighVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThreshold.setUnits("1/100 volts")


class _TnShelfLowVoltageThreshold_Type(Unsigned32):
    """Custom type tnShelfLowVoltageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8500),
    )


_TnShelfLowVoltageThreshold_Type.__name__ = "Unsigned32"
_TnShelfLowVoltageThreshold_Object = MibTableColumn
tnShelfLowVoltageThreshold = _TnShelfLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 23),
    _TnShelfLowVoltageThreshold_Type()
)
tnShelfLowVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThreshold.setUnits("1/100 volts")


class _TnShelfVoltageThresholdTol_Type(Unsigned32):
    """Custom type tnShelfVoltageThresholdTol based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_TnShelfVoltageThresholdTol_Type.__name__ = "Unsigned32"
_TnShelfVoltageThresholdTol_Object = MibTableColumn
tnShelfVoltageThresholdTol = _TnShelfVoltageThresholdTol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 24),
    _TnShelfVoltageThresholdTol_Type()
)
tnShelfVoltageThresholdTol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTol.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTol.setUnits("1/100 volts")


class _TnShelfExpectedVolts_Type(Integer32):
    """Custom type tnShelfExpectedVolts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v48", 1),
          ("v60", 2))
    )


_TnShelfExpectedVolts_Type.__name__ = "Integer32"
_TnShelfExpectedVolts_Object = MibTableColumn
tnShelfExpectedVolts = _TnShelfExpectedVolts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 25),
    _TnShelfExpectedVolts_Type()
)
tnShelfExpectedVolts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedVolts.setStatus("current")


class _TnShelfMatrixSize_Type(Integer32):
    """Custom type tnShelfMatrixSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ms1dot2T", 2),
          ("ms1dot9T", 3))
    )


_TnShelfMatrixSize_Type.__name__ = "Integer32"
_TnShelfMatrixSize_Object = MibTableColumn
tnShelfMatrixSize = _TnShelfMatrixSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 26),
    _TnShelfMatrixSize_Type()
)
tnShelfMatrixSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfMatrixSize.setStatus("current")


class _TnShelfVoltageFloor_Type(Unsigned32):
    """Custom type tnShelfVoltageFloor based on Unsigned32"""
    defaultValue = 3900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3900, 7200),
    )


_TnShelfVoltageFloor_Type.__name__ = "Unsigned32"
_TnShelfVoltageFloor_Object = MibTableColumn
tnShelfVoltageFloor = _TnShelfVoltageFloor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 27),
    _TnShelfVoltageFloor_Type()
)
tnShelfVoltageFloor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageFloor.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageFloor.setUnits("1/100 volts")
_TnShelfCalculatedLoad_Type = Unsigned32
_TnShelfCalculatedLoad_Object = MibTableColumn
tnShelfCalculatedLoad = _TnShelfCalculatedLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 28),
    _TnShelfCalculatedLoad_Type()
)
tnShelfCalculatedLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoad.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoad.setUnits("mA")


class _TnShelfClkSwitch_Type(AluWdmWtClkValues):
    """Custom type tnShelfClkSwitch based on AluWdmWtClkValues"""
    defaultValue = 1


_TnShelfClkSwitch_Type.__name__ = "AluWdmWtClkValues"
_TnShelfClkSwitch_Object = MibTableColumn
tnShelfClkSwitch = _TnShelfClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 29),
    _TnShelfClkSwitch_Type()
)
tnShelfClkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfClkSwitch.setStatus("current")


class _TnShelfExpectedVoltsAC_Type(Integer32):
    """Custom type tnShelfExpectedVoltsAC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v110", 1),
          ("v220", 2))
    )


_TnShelfExpectedVoltsAC_Type.__name__ = "Integer32"
_TnShelfExpectedVoltsAC_Object = MibTableColumn
tnShelfExpectedVoltsAC = _TnShelfExpectedVoltsAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 30),
    _TnShelfExpectedVoltsAC_Type()
)
tnShelfExpectedVoltsAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedVoltsAC.setStatus("current")


class _TnShelfHighVoltageThresholdAC_Type(Unsigned32):
    """Custom type tnShelfHighVoltageThresholdAC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 26400),
    )


_TnShelfHighVoltageThresholdAC_Type.__name__ = "Unsigned32"
_TnShelfHighVoltageThresholdAC_Object = MibTableColumn
tnShelfHighVoltageThresholdAC = _TnShelfHighVoltageThresholdAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 31),
    _TnShelfHighVoltageThresholdAC_Type()
)
tnShelfHighVoltageThresholdAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThresholdAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThresholdAC.setUnits("1/100 volts")


class _TnShelfLowVoltageThresholdAC_Type(Unsigned32):
    """Custom type tnShelfLowVoltageThresholdAC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 26400),
    )


_TnShelfLowVoltageThresholdAC_Type.__name__ = "Unsigned32"
_TnShelfLowVoltageThresholdAC_Object = MibTableColumn
tnShelfLowVoltageThresholdAC = _TnShelfLowVoltageThresholdAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 32),
    _TnShelfLowVoltageThresholdAC_Type()
)
tnShelfLowVoltageThresholdAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThresholdAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThresholdAC.setUnits("1/100 volts")


class _TnShelfVoltageFloorAC_Type(Unsigned32):
    """Custom type tnShelfVoltageFloorAC based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 26400),
    )


_TnShelfVoltageFloorAC_Type.__name__ = "Unsigned32"
_TnShelfVoltageFloorAC_Object = MibTableColumn
tnShelfVoltageFloorAC = _TnShelfVoltageFloorAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 33),
    _TnShelfVoltageFloorAC_Type()
)
tnShelfVoltageFloorAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageFloorAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageFloorAC.setUnits("1/100 volts")


class _TnShelfExternalAcPower_Type(Unsigned32):
    """Custom type tnShelfExternalAcPower based on Unsigned32"""
    defaultValue = 0


_TnShelfExternalAcPower_Type.__name__ = "Unsigned32"
_TnShelfExternalAcPower_Object = MibTableColumn
tnShelfExternalAcPower = _TnShelfExternalAcPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 34),
    _TnShelfExternalAcPower_Type()
)
tnShelfExternalAcPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExternalAcPower.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfExternalAcPower.setUnits("1/10 watt")


class _TnShelfLoadWarningThreshold_Type(Unsigned32):
    """Custom type tnShelfLoadWarningThreshold based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000),
    )


_TnShelfLoadWarningThreshold_Type.__name__ = "Unsigned32"
_TnShelfLoadWarningThreshold_Object = MibTableColumn
tnShelfLoadWarningThreshold = _TnShelfLoadWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 35),
    _TnShelfLoadWarningThreshold_Type()
)
tnShelfLoadWarningThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLoadWarningThreshold.setStatus("current")


class _TnShelfTimingSwitch_Type(Integer32):
    """Custom type tnShelfTimingSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timingSwitchAuto", 1),
          ("timingSwitchA", 2),
          ("timingSwitchB", 3))
    )


_TnShelfTimingSwitch_Type.__name__ = "Integer32"
_TnShelfTimingSwitch_Object = MibTableColumn
tnShelfTimingSwitch = _TnShelfTimingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 36),
    _TnShelfTimingSwitch_Type()
)
tnShelfTimingSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfTimingSwitch.setStatus("current")


class _TnShelfCalculatedLoadAC_Type(Unsigned32):
    """Custom type tnShelfCalculatedLoadAC based on Unsigned32"""
    defaultValue = 0


_TnShelfCalculatedLoadAC_Type.__name__ = "Unsigned32"
_TnShelfCalculatedLoadAC_Object = MibTableColumn
tnShelfCalculatedLoadAC = _TnShelfCalculatedLoadAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 37),
    _TnShelfCalculatedLoadAC_Type()
)
tnShelfCalculatedLoadAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoadAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoadAC.setUnits("mA")


class _TnShelfPowerCapacity_Type(Unsigned32):
    """Custom type tnShelfPowerCapacity based on Unsigned32"""
    defaultValue = 0


_TnShelfPowerCapacity_Type.__name__ = "Unsigned32"
_TnShelfPowerCapacity_Object = MibTableColumn
tnShelfPowerCapacity = _TnShelfPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 38),
    _TnShelfPowerCapacity_Type()
)
tnShelfPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfPowerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfPowerCapacity.setUnits("1/10 watt")


class _TnShelfRemainingPowerCapacity_Type(Integer32):
    """Custom type tnShelfRemainingPowerCapacity based on Integer32"""
    defaultValue = 0


_TnShelfRemainingPowerCapacity_Type.__name__ = "Integer32"
_TnShelfRemainingPowerCapacity_Object = MibTableColumn
tnShelfRemainingPowerCapacity = _TnShelfRemainingPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 39),
    _TnShelfRemainingPowerCapacity_Type()
)
tnShelfRemainingPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRemainingPowerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfRemainingPowerCapacity.setUnits("1/10 watt")


class _TnShelfLockout_Type(Integer32):
    """Custom type tnShelfLockout based on Integer32"""
    defaultValue = 4

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
        *(("fab07", 1),
          ("fab08", 2),
          ("fab09", 3),
          ("clear", 4))
    )


_TnShelfLockout_Type.__name__ = "Integer32"
_TnShelfLockout_Object = MibTableColumn
tnShelfLockout = _TnShelfLockout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 40),
    _TnShelfLockout_Type()
)
tnShelfLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLockout.setStatus("current")


class _TnShelfFilterMonitorStatus_Type(TruthValue):
    """Custom type tnShelfFilterMonitorStatus based on TruthValue"""
    defaultValue = 2


_TnShelfFilterMonitorStatus_Type.__name__ = "TruthValue"
_TnShelfFilterMonitorStatus_Object = MibTableColumn
tnShelfFilterMonitorStatus = _TnShelfFilterMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 41),
    _TnShelfFilterMonitorStatus_Type()
)
tnShelfFilterMonitorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterMonitorStatus.setStatus("current")


class _TnShelfFilterInspectionInterval_Type(Unsigned32):
    """Custom type tnShelfFilterInspectionInterval based on Unsigned32"""
    defaultValue = 26

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104),
    )


_TnShelfFilterInspectionInterval_Type.__name__ = "Unsigned32"
_TnShelfFilterInspectionInterval_Object = MibTableColumn
tnShelfFilterInspectionInterval = _TnShelfFilterInspectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 42),
    _TnShelfFilterInspectionInterval_Type()
)
tnShelfFilterInspectionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterInspectionInterval.setStatus("current")


class _TnShelfFilterStartDate_Type(Unsigned32):
    """Custom type tnShelfFilterStartDate based on Unsigned32"""
    defaultValue = 426770689


_TnShelfFilterStartDate_Type.__name__ = "Unsigned32"
_TnShelfFilterStartDate_Object = MibTableColumn
tnShelfFilterStartDate = _TnShelfFilterStartDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 43),
    _TnShelfFilterStartDate_Type()
)
tnShelfFilterStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterStartDate.setStatus("current")
_TnShelfAlmProfName_Type = OctetString
_TnShelfAlmProfName_Object = MibTableColumn
tnShelfAlmProfName = _TnShelfAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 44),
    _TnShelfAlmProfName_Type()
)
tnShelfAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfAlmProfName.setStatus("current")


class _TnShelfBranchPowerCap1_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap1 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap1_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap1_Object = MibTableColumn
tnShelfBranchPowerCap1 = _TnShelfBranchPowerCap1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 45),
    _TnShelfBranchPowerCap1_Type()
)
tnShelfBranchPowerCap1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap1.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap1.setUnits("1/10 watt")


class _TnShelfBranchPowerCap2_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap2 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap2_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap2_Object = MibTableColumn
tnShelfBranchPowerCap2 = _TnShelfBranchPowerCap2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 46),
    _TnShelfBranchPowerCap2_Type()
)
tnShelfBranchPowerCap2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap2.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap2.setUnits("1/10 watt")


class _TnShelfBranchPowerCap3_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap3 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap3_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap3_Object = MibTableColumn
tnShelfBranchPowerCap3 = _TnShelfBranchPowerCap3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 47),
    _TnShelfBranchPowerCap3_Type()
)
tnShelfBranchPowerCap3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap3.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap3.setUnits("1/10 watt")


class _TnShelfBranchPowerCap4_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap4 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap4_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap4_Object = MibTableColumn
tnShelfBranchPowerCap4 = _TnShelfBranchPowerCap4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 48),
    _TnShelfBranchPowerCap4_Type()
)
tnShelfBranchPowerCap4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap4.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap4.setUnits("1/10 watt")


class _TnShelfBranchPowerCap5_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap5 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap5_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap5_Object = MibTableColumn
tnShelfBranchPowerCap5 = _TnShelfBranchPowerCap5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 49),
    _TnShelfBranchPowerCap5_Type()
)
tnShelfBranchPowerCap5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap5.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap5.setUnits("1/10 watt")


class _TnShelfBranchPowerCap6_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap6 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap6_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap6_Object = MibTableColumn
tnShelfBranchPowerCap6 = _TnShelfBranchPowerCap6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 50),
    _TnShelfBranchPowerCap6_Type()
)
tnShelfBranchPowerCap6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap6.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap6.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap1_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap1 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap1_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap1_Object = MibTableColumn
tnShelfBranchRemainingPwrCap1 = _TnShelfBranchRemainingPwrCap1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 51),
    _TnShelfBranchRemainingPwrCap1_Type()
)
tnShelfBranchRemainingPwrCap1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap1.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap1.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap2_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap2 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap2_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap2_Object = MibTableColumn
tnShelfBranchRemainingPwrCap2 = _TnShelfBranchRemainingPwrCap2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 52),
    _TnShelfBranchRemainingPwrCap2_Type()
)
tnShelfBranchRemainingPwrCap2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap2.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap2.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap3_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap3 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap3_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap3_Object = MibTableColumn
tnShelfBranchRemainingPwrCap3 = _TnShelfBranchRemainingPwrCap3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 53),
    _TnShelfBranchRemainingPwrCap3_Type()
)
tnShelfBranchRemainingPwrCap3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap3.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap3.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap4_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap4 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap4_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap4_Object = MibTableColumn
tnShelfBranchRemainingPwrCap4 = _TnShelfBranchRemainingPwrCap4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 54),
    _TnShelfBranchRemainingPwrCap4_Type()
)
tnShelfBranchRemainingPwrCap4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap4.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap4.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap5_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap5 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap5_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap5_Object = MibTableColumn
tnShelfBranchRemainingPwrCap5 = _TnShelfBranchRemainingPwrCap5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 55),
    _TnShelfBranchRemainingPwrCap5_Type()
)
tnShelfBranchRemainingPwrCap5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap5.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap5.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap6_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap6 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap6_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap6_Object = MibTableColumn
tnShelfBranchRemainingPwrCap6 = _TnShelfBranchRemainingPwrCap6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 56),
    _TnShelfBranchRemainingPwrCap6_Type()
)
tnShelfBranchRemainingPwrCap6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap6.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap6.setUnits("1/10 watt")


class _TnShelfFabricEQPStatus_Type(Integer32):
    """Custom type tnShelfFabricEQPStatus based on Integer32"""
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
        *(("available", 1),
          ("notAvailable", 2),
          ("inUse", 3),
          ("trafficImpaired", 4),
          ("allTrafficLost", 5))
    )


_TnShelfFabricEQPStatus_Type.__name__ = "Integer32"
_TnShelfFabricEQPStatus_Object = MibTableColumn
tnShelfFabricEQPStatus = _TnShelfFabricEQPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 57),
    _TnShelfFabricEQPStatus_Type()
)
tnShelfFabricEQPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricEQPStatus.setStatus("current")


class _TnShelfFabricActivityState_Type(Integer32):
    """Custom type tnShelfFabricActivityState based on Integer32"""
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
        *(("inUse", 1),
          ("notInUse", 2),
          ("lockedOut", 3),
          ("loButInUse", 4))
    )


_TnShelfFabricActivityState_Type.__name__ = "Integer32"
_TnShelfFabricActivityState_Object = MibTableColumn
tnShelfFabricActivityState = _TnShelfFabricActivityState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 58),
    _TnShelfFabricActivityState_Type()
)
tnShelfFabricActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricActivityState.setStatus("current")


class _TnShelfFabricFailures_Type(Integer32):
    """Custom type tnShelfFabricFailures based on Integer32"""
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
        *(("none", 1),
          ("tSIFail", 2),
          ("linkFail", 3),
          ("cardFail", 4),
          ("cardRemoved", 5),
          ("latchOpen", 6))
    )


_TnShelfFabricFailures_Type.__name__ = "Integer32"
_TnShelfFabricFailures_Object = MibTableColumn
tnShelfFabricFailures = _TnShelfFabricFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 59),
    _TnShelfFabricFailures_Type()
)
tnShelfFabricFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricFailures.setStatus("current")


class _TnShelfFabricUsage_Type(Integer32):
    """Custom type tnShelfFabricUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_TnShelfFabricUsage_Type.__name__ = "Integer32"
_TnShelfFabricUsage_Object = MibTableColumn
tnShelfFabricUsage = _TnShelfFabricUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 60),
    _TnShelfFabricUsage_Type()
)
tnShelfFabricUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricUsage.setStatus("current")
_TnShelfFabricEqpsLEDColor_Type = OctetString
_TnShelfFabricEqpsLEDColor_Object = MibTableColumn
tnShelfFabricEqpsLEDColor = _TnShelfFabricEqpsLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 61),
    _TnShelfFabricEqpsLEDColor_Type()
)
tnShelfFabricEqpsLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricEqpsLEDColor.setStatus("current")


class _TnShelfFabricReadyToProtect_Type(Integer32):
    """Custom type tnShelfFabricReadyToProtect based on Integer32"""
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
        *(("yes", 1),
          ("partially", 2),
          ("no", 3),
          ("invalid", 4))
    )


_TnShelfFabricReadyToProtect_Type.__name__ = "Integer32"
_TnShelfFabricReadyToProtect_Object = MibTableColumn
tnShelfFabricReadyToProtect = _TnShelfFabricReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 62),
    _TnShelfFabricReadyToProtect_Type()
)
tnShelfFabricReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricReadyToProtect.setStatus("current")


class _TnShelfRackType_Type(TnRackSize):
    """Custom type tnShelfRackType based on TnRackSize"""
    defaultValue = 1


_TnShelfRackType_Type.__name__ = "TnRackSize"
_TnShelfRackType_Object = MibTableColumn
tnShelfRackType = _TnShelfRackType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 63),
    _TnShelfRackType_Type()
)
tnShelfRackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRackType.setStatus("current")


class _TnShelfInventoryAction_Type(Integer32):
    """Custom type tnShelfInventoryAction based on Integer32"""
    defaultValue = 1

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
        *(("unInitialized", 1),
          ("toDb", 2),
          ("toHw", 3),
          ("ready", 4),
          ("fail", 5))
    )


_TnShelfInventoryAction_Type.__name__ = "Integer32"
_TnShelfInventoryAction_Object = MibTableColumn
tnShelfInventoryAction = _TnShelfInventoryAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 64),
    _TnShelfInventoryAction_Type()
)
tnShelfInventoryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfInventoryAction.setStatus("current")
_TnShelfTotal_Type = Integer32
_TnShelfTotal_Object = MibScalar
tnShelfTotal = _TnShelfTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 2),
    _TnShelfTotal_Type()
)
tnShelfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfTotal.setStatus("current")
_TnShelfRiDataTable_Object = MibTable
tnShelfRiDataTable = _TnShelfRiDataTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnShelfRiDataTable.setStatus("current")
_TnShelfRiDataEntry_Object = MibTableRow
tnShelfRiDataEntry = _TnShelfRiDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1)
)
tnShelfRiDataEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfRiDataEntry.setStatus("current")


class _TnShelfRiCompanyID_Type(SnmpAdminString):
    """Custom type tnShelfRiCompanyID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiCompanyID_Type.__name__ = "SnmpAdminString"
_TnShelfRiCompanyID_Object = MibTableColumn
tnShelfRiCompanyID = _TnShelfRiCompanyID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 1),
    _TnShelfRiCompanyID_Type()
)
tnShelfRiCompanyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiCompanyID.setStatus("current")


class _TnShelfRiMnemonic_Type(SnmpAdminString):
    """Custom type tnShelfRiMnemonic based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiMnemonic_Type.__name__ = "SnmpAdminString"
_TnShelfRiMnemonic_Object = MibTableColumn
tnShelfRiMnemonic = _TnShelfRiMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 2),
    _TnShelfRiMnemonic_Type()
)
tnShelfRiMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiMnemonic.setStatus("current")


class _TnShelfRiCLEI_Type(TropicCardCLEI):
    """Custom type tnShelfRiCLEI based on TropicCardCLEI"""
    defaultValue = OctetString("")


_TnShelfRiCLEI_Type.__name__ = "TropicCardCLEI"
_TnShelfRiCLEI_Object = MibTableColumn
tnShelfRiCLEI = _TnShelfRiCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 3),
    _TnShelfRiCLEI_Type()
)
tnShelfRiCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiCLEI.setStatus("current")


class _TnShelfRiManufacturingPartNumber_Type(TropicCardManufacturingPartNumber):
    """Custom type tnShelfRiManufacturingPartNumber based on TropicCardManufacturingPartNumber"""
    defaultValue = OctetString("")


_TnShelfRiManufacturingPartNumber_Type.__name__ = "TropicCardManufacturingPartNumber"
_TnShelfRiManufacturingPartNumber_Object = MibTableColumn
tnShelfRiManufacturingPartNumber = _TnShelfRiManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 4),
    _TnShelfRiManufacturingPartNumber_Type()
)
tnShelfRiManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiManufacturingPartNumber.setStatus("current")


class _TnShelfRiSWPartNum_Type(SnmpAdminString):
    """Custom type tnShelfRiSWPartNum based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiSWPartNum_Type.__name__ = "SnmpAdminString"
_TnShelfRiSWPartNum_Object = MibTableColumn
tnShelfRiSWPartNum = _TnShelfRiSWPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 5),
    _TnShelfRiSWPartNum_Type()
)
tnShelfRiSWPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiSWPartNum.setStatus("current")


class _TnShelfRiFactoryID_Type(SnmpAdminString):
    """Custom type tnShelfRiFactoryID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiFactoryID_Type.__name__ = "SnmpAdminString"
_TnShelfRiFactoryID_Object = MibTableColumn
tnShelfRiFactoryID = _TnShelfRiFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 6),
    _TnShelfRiFactoryID_Type()
)
tnShelfRiFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiFactoryID.setStatus("current")


class _TnShelfRiSerialNumber_Type(TropicCardSerialNumber):
    """Custom type tnShelfRiSerialNumber based on TropicCardSerialNumber"""
    defaultValue = OctetString("")


_TnShelfRiSerialNumber_Type.__name__ = "TropicCardSerialNumber"
_TnShelfRiSerialNumber_Object = MibTableColumn
tnShelfRiSerialNumber = _TnShelfRiSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 7),
    _TnShelfRiSerialNumber_Type()
)
tnShelfRiSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiSerialNumber.setStatus("current")


class _TnShelfRiDate_Type(SnmpAdminString):
    """Custom type tnShelfRiDate based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiDate_Type.__name__ = "SnmpAdminString"
_TnShelfRiDate_Object = MibTableColumn
tnShelfRiDate = _TnShelfRiDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 8),
    _TnShelfRiDate_Type()
)
tnShelfRiDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiDate.setStatus("current")


class _TnShelfRiExtraData_Type(SnmpAdminString):
    """Custom type tnShelfRiExtraData based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiExtraData_Type.__name__ = "SnmpAdminString"
_TnShelfRiExtraData_Object = MibTableColumn
tnShelfRiExtraData = _TnShelfRiExtraData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 9),
    _TnShelfRiExtraData_Type()
)
tnShelfRiExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiExtraData.setStatus("current")

# Managed Objects groups

tnShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 1)
)
tnShelfGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfName"),
        ("TROPIC-SHELF-MIB", "tnShelfDescr"),
        ("TROPIC-SHELF-MIB", "tnShelfSerialNum"),
        ("TROPIC-SHELF-MIB", "tnShelfProgrammedType"),
        ("TROPIC-SHELF-MIB", "tnShelfPresentType"),
        ("TROPIC-SHELF-MIB", "tnShelfActivitySwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfLampTest"),
        ("TROPIC-SHELF-MIB", "tnShelfMateCCReadyToProtect"),
        ("TROPIC-SHELF-MIB", "tnShelfIsUnmanaged"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedAmps"),
        ("TROPIC-SHELF-MIB", "tnShelfSerialNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfAINS"),
        ("TROPIC-SHELF-MIB", "tnShelfStatusLEDColor"),
        ("TROPIC-SHELF-MIB", "tnShelfStatusLEDState"),
        ("TROPIC-SHELF-MIB", "tnShelfWTMode"),
        ("TROPIC-SHELF-MIB", "tnShelfActivityMt0cSwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfMateMt0cReadyToProtect"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedPfa"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedPfb"),
        ("TROPIC-SHELF-MIB", "tnShelfHighVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfLowVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageThresholdTol"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedVolts"),
        ("TROPIC-SHELF-MIB", "tnShelfMatrixSize"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageFloor"),
        ("TROPIC-SHELF-MIB", "tnShelfCalculatedLoad"),
        ("TROPIC-SHELF-MIB", "tnShelfClkSwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedVoltsAC"),
        ("TROPIC-SHELF-MIB", "tnShelfHighVoltageThresholdAC"),
        ("TROPIC-SHELF-MIB", "tnShelfLowVoltageThresholdAC"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageFloorAC"),
        ("TROPIC-SHELF-MIB", "tnShelfExternalAcPower"),
        ("TROPIC-SHELF-MIB", "tnShelfLoadWarningThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfTimingSwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfCalculatedLoadAC"),
        ("TROPIC-SHELF-MIB", "tnShelfPowerCapacity"),
        ("TROPIC-SHELF-MIB", "tnShelfRemainingPowerCapacity"),
        ("TROPIC-SHELF-MIB", "tnShelfLockout"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterMonitorStatus"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterInspectionInterval"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterStartDate"),
        ("TROPIC-SHELF-MIB", "tnShelfAlmProfName"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap1"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap2"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap3"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap4"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap5"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap6"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap1"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap2"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap3"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap4"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap5"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap6"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricEQPStatus"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricActivityState"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricFailures"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricUsage"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricEqpsLEDColor"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricReadyToProtect"),
        ("TROPIC-SHELF-MIB", "tnShelfRackType"),
        ("TROPIC-SHELF-MIB", "tnShelfInventoryAction"))
)
if mibBuilder.loadTexts:
    tnShelfGroup.setStatus("current")

tnShelfScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 2)
)
tnShelfScalarsGroup.setObjects(
    ("TROPIC-SHELF-MIB", "tnShelfTotal")
)
if mibBuilder.loadTexts:
    tnShelfScalarsGroup.setStatus("current")

tnShelfRiDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 3)
)
tnShelfRiDataGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfRiCompanyID"),
        ("TROPIC-SHELF-MIB", "tnShelfRiMnemonic"),
        ("TROPIC-SHELF-MIB", "tnShelfRiCLEI"),
        ("TROPIC-SHELF-MIB", "tnShelfRiManufacturingPartNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfRiSWPartNum"),
        ("TROPIC-SHELF-MIB", "tnShelfRiFactoryID"),
        ("TROPIC-SHELF-MIB", "tnShelfRiSerialNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfRiDate"),
        ("TROPIC-SHELF-MIB", "tnShelfRiExtraData"))
)
if mibBuilder.loadTexts:
    tnShelfRiDataGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnShelfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 2, 1)
)
tnShelfCompliance.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfScalarsGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfRiDataGroup"))
)
if mibBuilder.loadTexts:
    tnShelfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SHELF-MIB",
    **{"AluWdmExpectedAmpPF": AluWdmExpectedAmpPF,
       "tnShelfMibModule": tnShelfMibModule,
       "tnShelfConf": tnShelfConf,
       "tnShelfGroups": tnShelfGroups,
       "tnShelfGroup": tnShelfGroup,
       "tnShelfScalarsGroup": tnShelfScalarsGroup,
       "tnShelfRiDataGroup": tnShelfRiDataGroup,
       "tnShelfCompliances": tnShelfCompliances,
       "tnShelfCompliance": tnShelfCompliance,
       "tnShelfObjs": tnShelfObjs,
       "tnShelfBasics": tnShelfBasics,
       "tnShelfTable": tnShelfTable,
       "tnShelfEntry": tnShelfEntry,
       "tnShelfIndex": tnShelfIndex,
       "tnShelfName": tnShelfName,
       "tnShelfDescr": tnShelfDescr,
       "tnShelfSerialNum": tnShelfSerialNum,
       "tnShelfProgrammedType": tnShelfProgrammedType,
       "tnShelfPresentType": tnShelfPresentType,
       "tnShelfActivitySwitch": tnShelfActivitySwitch,
       "tnShelfLampTest": tnShelfLampTest,
       "tnShelfMateCCReadyToProtect": tnShelfMateCCReadyToProtect,
       "tnShelfIsUnmanaged": tnShelfIsUnmanaged,
       "tnShelfExpectedAmps": tnShelfExpectedAmps,
       "tnShelfSerialNumber": tnShelfSerialNumber,
       "tnShelfAINS": tnShelfAINS,
       "tnShelfStatusLEDColor": tnShelfStatusLEDColor,
       "tnShelfStatusLEDState": tnShelfStatusLEDState,
       "tnShelfWTMode": tnShelfWTMode,
       "tnShelfActivityMt0cSwitch": tnShelfActivityMt0cSwitch,
       "tnShelfMateMt0cReadyToProtect": tnShelfMateMt0cReadyToProtect,
       "tnShelfExpectedPfa": tnShelfExpectedPfa,
       "tnShelfExpectedPfb": tnShelfExpectedPfb,
       "tnShelfHighVoltageThreshold": tnShelfHighVoltageThreshold,
       "tnShelfLowVoltageThreshold": tnShelfLowVoltageThreshold,
       "tnShelfVoltageThresholdTol": tnShelfVoltageThresholdTol,
       "tnShelfExpectedVolts": tnShelfExpectedVolts,
       "tnShelfMatrixSize": tnShelfMatrixSize,
       "tnShelfVoltageFloor": tnShelfVoltageFloor,
       "tnShelfCalculatedLoad": tnShelfCalculatedLoad,
       "tnShelfClkSwitch": tnShelfClkSwitch,
       "tnShelfExpectedVoltsAC": tnShelfExpectedVoltsAC,
       "tnShelfHighVoltageThresholdAC": tnShelfHighVoltageThresholdAC,
       "tnShelfLowVoltageThresholdAC": tnShelfLowVoltageThresholdAC,
       "tnShelfVoltageFloorAC": tnShelfVoltageFloorAC,
       "tnShelfExternalAcPower": tnShelfExternalAcPower,
       "tnShelfLoadWarningThreshold": tnShelfLoadWarningThreshold,
       "tnShelfTimingSwitch": tnShelfTimingSwitch,
       "tnShelfCalculatedLoadAC": tnShelfCalculatedLoadAC,
       "tnShelfPowerCapacity": tnShelfPowerCapacity,
       "tnShelfRemainingPowerCapacity": tnShelfRemainingPowerCapacity,
       "tnShelfLockout": tnShelfLockout,
       "tnShelfFilterMonitorStatus": tnShelfFilterMonitorStatus,
       "tnShelfFilterInspectionInterval": tnShelfFilterInspectionInterval,
       "tnShelfFilterStartDate": tnShelfFilterStartDate,
       "tnShelfAlmProfName": tnShelfAlmProfName,
       "tnShelfBranchPowerCap1": tnShelfBranchPowerCap1,
       "tnShelfBranchPowerCap2": tnShelfBranchPowerCap2,
       "tnShelfBranchPowerCap3": tnShelfBranchPowerCap3,
       "tnShelfBranchPowerCap4": tnShelfBranchPowerCap4,
       "tnShelfBranchPowerCap5": tnShelfBranchPowerCap5,
       "tnShelfBranchPowerCap6": tnShelfBranchPowerCap6,
       "tnShelfBranchRemainingPwrCap1": tnShelfBranchRemainingPwrCap1,
       "tnShelfBranchRemainingPwrCap2": tnShelfBranchRemainingPwrCap2,
       "tnShelfBranchRemainingPwrCap3": tnShelfBranchRemainingPwrCap3,
       "tnShelfBranchRemainingPwrCap4": tnShelfBranchRemainingPwrCap4,
       "tnShelfBranchRemainingPwrCap5": tnShelfBranchRemainingPwrCap5,
       "tnShelfBranchRemainingPwrCap6": tnShelfBranchRemainingPwrCap6,
       "tnShelfFabricEQPStatus": tnShelfFabricEQPStatus,
       "tnShelfFabricActivityState": tnShelfFabricActivityState,
       "tnShelfFabricFailures": tnShelfFabricFailures,
       "tnShelfFabricUsage": tnShelfFabricUsage,
       "tnShelfFabricEqpsLEDColor": tnShelfFabricEqpsLEDColor,
       "tnShelfFabricReadyToProtect": tnShelfFabricReadyToProtect,
       "tnShelfRackType": tnShelfRackType,
       "tnShelfInventoryAction": tnShelfInventoryAction,
       "tnShelfTotal": tnShelfTotal,
       "tnShelfRiDataTable": tnShelfRiDataTable,
       "tnShelfRiDataEntry": tnShelfRiDataEntry,
       "tnShelfRiCompanyID": tnShelfRiCompanyID,
       "tnShelfRiMnemonic": tnShelfRiMnemonic,
       "tnShelfRiCLEI": tnShelfRiCLEI,
       "tnShelfRiManufacturingPartNumber": tnShelfRiManufacturingPartNumber,
       "tnShelfRiSWPartNum": tnShelfRiSWPartNum,
       "tnShelfRiFactoryID": tnShelfRiFactoryID,
       "tnShelfRiSerialNumber": tnShelfRiSerialNumber,
       "tnShelfRiDate": tnShelfRiDate,
       "tnShelfRiExtraData": tnShelfRiExtraData}
)
