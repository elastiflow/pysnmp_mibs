# SNMP MIB module (PEAKDBU200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKDBU200-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(FaultType,
 OnOffType,
 RemoteLocalType,
 indvUnits) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "FaultType",
    "OnOffType",
    "RemoteLocalType",
    "indvUnits")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

peakDBU200Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002)
)
if mibBuilder.loadTexts:
    peakDBU200Module.setRevisions(
        ("2015-09-15 09:00",
         "2013-04-04 12:00",
         "2013-03-14 12:00",
         "2010-08-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Dbu200AutoSwType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unit1", 1),
          ("auto", 2),
          ("unit2", 3))
    )



class Dbu200BandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unit1", 1),
          ("unit2", 2),
          ("unknown", 3))
    )



class Dbu200PresentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2),
          ("unknown", 3))
    )



class Dbu200ExtRefType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Dbu200Type_Type = OctetString
_Dbu200Type_Object = MibScalar
dbu200Type = _Dbu200Type_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 1),
    _Dbu200Type_Type()
)
dbu200Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Type.setStatus("current")


class _Dbu200SerialNo_Type(Integer32):
    """Custom type dbu200SerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Dbu200SerialNo_Type.__name__ = "Integer32"
_Dbu200SerialNo_Object = MibScalar
dbu200SerialNo = _Dbu200SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 2),
    _Dbu200SerialNo_Type()
)
dbu200SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200SerialNo.setStatus("current")
_Dbu200SoftwareVersion_Type = OctetString
_Dbu200SoftwareVersion_Object = MibScalar
dbu200SoftwareVersion = _Dbu200SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 3),
    _Dbu200SoftwareVersion_Type()
)
dbu200SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200SoftwareVersion.setStatus("current")
_Dbu200Remote_Type = RemoteLocalType
_Dbu200Remote_Object = MibScalar
dbu200Remote = _Dbu200Remote_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 4),
    _Dbu200Remote_Type()
)
dbu200Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Remote.setStatus("current")
_Dbu200AutoSwitch_Type = Dbu200AutoSwType
_Dbu200AutoSwitch_Object = MibScalar
dbu200AutoSwitch = _Dbu200AutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 5),
    _Dbu200AutoSwitch_Type()
)
dbu200AutoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbu200AutoSwitch.setStatus("current")
_Dbu200Band_Type = Dbu200BandType
_Dbu200Band_Object = MibScalar
dbu200Band = _Dbu200Band_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 6),
    _Dbu200Band_Type()
)
dbu200Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Band.setStatus("current")
_Dbu200Unit1_Type = OnOffType
_Dbu200Unit1_Object = MibScalar
dbu200Unit1 = _Dbu200Unit1_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 7),
    _Dbu200Unit1_Type()
)
dbu200Unit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit1.setStatus("current")
_Dbu200Unit2_Type = OnOffType
_Dbu200Unit2_Object = MibScalar
dbu200Unit2 = _Dbu200Unit2_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 8),
    _Dbu200Unit2_Type()
)
dbu200Unit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit2.setStatus("current")
_Dbu200Unit1Alarm_Type = FaultType
_Dbu200Unit1Alarm_Object = MibScalar
dbu200Unit1Alarm = _Dbu200Unit1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 9),
    _Dbu200Unit1Alarm_Type()
)
dbu200Unit1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit1Alarm.setStatus("current")
_Dbu200Unit2Alarm_Type = FaultType
_Dbu200Unit2Alarm_Object = MibScalar
dbu200Unit2Alarm = _Dbu200Unit2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 10),
    _Dbu200Unit2Alarm_Type()
)
dbu200Unit2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit2Alarm.setStatus("current")
_Dbu200SummaryAlarm_Type = FaultType
_Dbu200SummaryAlarm_Object = MibScalar
dbu200SummaryAlarm = _Dbu200SummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 11),
    _Dbu200SummaryAlarm_Type()
)
dbu200SummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200SummaryAlarm.setStatus("current")
_Dbu200PSU1Alarm_Type = FaultType
_Dbu200PSU1Alarm_Object = MibScalar
dbu200PSU1Alarm = _Dbu200PSU1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 12),
    _Dbu200PSU1Alarm_Type()
)
dbu200PSU1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200PSU1Alarm.setStatus("current")
_Dbu200PSU2Alarm_Type = FaultType
_Dbu200PSU2Alarm_Object = MibScalar
dbu200PSU2Alarm = _Dbu200PSU2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 13),
    _Dbu200PSU2Alarm_Type()
)
dbu200PSU2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200PSU2Alarm.setStatus("current")
_Dbu200Address_Type = FaultType
_Dbu200Address_Object = MibScalar
dbu200Address = _Dbu200Address_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 14),
    _Dbu200Address_Type()
)
dbu200Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Address.setStatus("current")
_Dbu200Unit1Present_Type = Dbu200PresentType
_Dbu200Unit1Present_Object = MibScalar
dbu200Unit1Present = _Dbu200Unit1Present_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 15),
    _Dbu200Unit1Present_Type()
)
dbu200Unit1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit1Present.setStatus("current")
_Dbu200Unit2Present_Type = Dbu200PresentType
_Dbu200Unit2Present_Object = MibScalar
dbu200Unit2Present = _Dbu200Unit2Present_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 16),
    _Dbu200Unit2Present_Type()
)
dbu200Unit2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit2Present.setStatus("current")
_Dbu200Unit1ExtRef_Type = Dbu200ExtRefType
_Dbu200Unit1ExtRef_Object = MibScalar
dbu200Unit1ExtRef = _Dbu200Unit1ExtRef_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 17),
    _Dbu200Unit1ExtRef_Type()
)
dbu200Unit1ExtRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit1ExtRef.setStatus("current")
_Dbu200Unit2ExtRef_Type = Dbu200ExtRefType
_Dbu200Unit2ExtRef_Object = MibScalar
dbu200Unit2ExtRef = _Dbu200Unit2ExtRef_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 18),
    _Dbu200Unit2ExtRef_Type()
)
dbu200Unit2ExtRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbu200Unit2ExtRef.setStatus("current")
_Dbu200ConvGroups_ObjectIdentity = ObjectIdentity
dbu200ConvGroups = _Dbu200ConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 110)
)
_Dbu200ConvConformance_ObjectIdentity = ObjectIdentity
dbu200ConvConformance = _Dbu200ConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 111)
)

# Managed Objects groups

dbu200CNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 110, 1)
)
dbu200CNFReqGrp.setObjects(
      *(("PEAKDBU200-MIB", "dbu200Type"),
        ("PEAKDBU200-MIB", "dbu200SerialNo"),
        ("PEAKDBU200-MIB", "dbu200SoftwareVersion"),
        ("PEAKDBU200-MIB", "dbu200Remote"),
        ("PEAKDBU200-MIB", "dbu200AutoSwitch"),
        ("PEAKDBU200-MIB", "dbu200Band"),
        ("PEAKDBU200-MIB", "dbu200Unit1"),
        ("PEAKDBU200-MIB", "dbu200Unit2"),
        ("PEAKDBU200-MIB", "dbu200Unit1Alarm"),
        ("PEAKDBU200-MIB", "dbu200Unit2Alarm"),
        ("PEAKDBU200-MIB", "dbu200SummaryAlarm"),
        ("PEAKDBU200-MIB", "dbu200PSU1Alarm"),
        ("PEAKDBU200-MIB", "dbu200PSU2Alarm"),
        ("PEAKDBU200-MIB", "dbu200Address"),
        ("PEAKDBU200-MIB", "dbu200Unit1Present"),
        ("PEAKDBU200-MIB", "dbu200Unit2Present"),
        ("PEAKDBU200-MIB", "dbu200Unit1ExtRef"),
        ("PEAKDBU200-MIB", "dbu200Unit2ExtRef"))
)
if mibBuilder.loadTexts:
    dbu200CNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dbu200CNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8002, 111, 1)
)
dbu200CNFCompliance.setObjects(
    ("PEAKDBU200-MIB", "dbu200CNFReqGrp")
)
if mibBuilder.loadTexts:
    dbu200CNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKDBU200-MIB",
    **{"Dbu200AutoSwType": Dbu200AutoSwType,
       "Dbu200BandType": Dbu200BandType,
       "Dbu200PresentType": Dbu200PresentType,
       "Dbu200ExtRefType": Dbu200ExtRefType,
       "peakDBU200Module": peakDBU200Module,
       "dbu200Type": dbu200Type,
       "dbu200SerialNo": dbu200SerialNo,
       "dbu200SoftwareVersion": dbu200SoftwareVersion,
       "dbu200Remote": dbu200Remote,
       "dbu200AutoSwitch": dbu200AutoSwitch,
       "dbu200Band": dbu200Band,
       "dbu200Unit1": dbu200Unit1,
       "dbu200Unit2": dbu200Unit2,
       "dbu200Unit1Alarm": dbu200Unit1Alarm,
       "dbu200Unit2Alarm": dbu200Unit2Alarm,
       "dbu200SummaryAlarm": dbu200SummaryAlarm,
       "dbu200PSU1Alarm": dbu200PSU1Alarm,
       "dbu200PSU2Alarm": dbu200PSU2Alarm,
       "dbu200Address": dbu200Address,
       "dbu200Unit1Present": dbu200Unit1Present,
       "dbu200Unit2Present": dbu200Unit2Present,
       "dbu200Unit1ExtRef": dbu200Unit1ExtRef,
       "dbu200Unit2ExtRef": dbu200Unit2ExtRef,
       "dbu200ConvGroups": dbu200ConvGroups,
       "dbu200CNFReqGrp": dbu200CNFReqGrp,
       "dbu200ConvConformance": dbu200ConvConformance,
       "dbu200CNFCompliance": dbu200CNFCompliance}
)
