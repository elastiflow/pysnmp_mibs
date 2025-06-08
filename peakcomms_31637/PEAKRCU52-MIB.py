# SNMP MIB module (PEAKRCU52-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKRCU52-MIB.mib
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

peakRCU52Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025)
)
if mibBuilder.loadTexts:
    peakRCU52Module.setRevisions(
        ("2016-08-12 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rcu52AutoSwType(TextualConvention, Integer32):
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
        *(("unitA", 1),
          ("auto", 2),
          ("unitB", 3))
    )



class Rcu52StandbyPositionType(TextualConvention, Integer32):
    status = "current"
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
        *(("unitA", 1),
          ("unitB", 2),
          ("unitStandby", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Rcu52Type_Type = OctetString
_Rcu52Type_Object = MibScalar
rcu52Type = _Rcu52Type_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 1),
    _Rcu52Type_Type()
)
rcu52Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52Type.setStatus("current")


class _Rcu52SerialNo_Type(Integer32):
    """Custom type rcu52SerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rcu52SerialNo_Type.__name__ = "Integer32"
_Rcu52SerialNo_Object = MibScalar
rcu52SerialNo = _Rcu52SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 2),
    _Rcu52SerialNo_Type()
)
rcu52SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52SerialNo.setStatus("current")
_Rcu52SoftwareVersion_Type = OctetString
_Rcu52SoftwareVersion_Object = MibScalar
rcu52SoftwareVersion = _Rcu52SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 3),
    _Rcu52SoftwareVersion_Type()
)
rcu52SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52SoftwareVersion.setStatus("current")
_Rcu52Remote_Type = RemoteLocalType
_Rcu52Remote_Object = MibScalar
rcu52Remote = _Rcu52Remote_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 4),
    _Rcu52Remote_Type()
)
rcu52Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52Remote.setStatus("current")
_Rcu52AutoSwitch_Type = Rcu52AutoSwType
_Rcu52AutoSwitch_Object = MibScalar
rcu52AutoSwitch = _Rcu52AutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 5),
    _Rcu52AutoSwitch_Type()
)
rcu52AutoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu52AutoSwitch.setStatus("current")
_Rcu52StandbyPosition_Type = Rcu52StandbyPositionType
_Rcu52StandbyPosition_Object = MibScalar
rcu52StandbyPosition = _Rcu52StandbyPosition_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 6),
    _Rcu52StandbyPosition_Type()
)
rcu52StandbyPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52StandbyPosition.setStatus("current")
_Rcu52UnitA_Type = OnOffType
_Rcu52UnitA_Object = MibScalar
rcu52UnitA = _Rcu52UnitA_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 7),
    _Rcu52UnitA_Type()
)
rcu52UnitA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52UnitA.setStatus("current")
_Rcu52UnitB_Type = OnOffType
_Rcu52UnitB_Object = MibScalar
rcu52UnitB = _Rcu52UnitB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 8),
    _Rcu52UnitB_Type()
)
rcu52UnitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52UnitB.setStatus("current")
_Rcu52UnitStandby_Type = OnOffType
_Rcu52UnitStandby_Object = MibScalar
rcu52UnitStandby = _Rcu52UnitStandby_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 9),
    _Rcu52UnitStandby_Type()
)
rcu52UnitStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52UnitStandby.setStatus("current")
_Rcu52SummaryAlarm_Type = FaultType
_Rcu52SummaryAlarm_Object = MibScalar
rcu52SummaryAlarm = _Rcu52SummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 10),
    _Rcu52SummaryAlarm_Type()
)
rcu52SummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu52SummaryAlarm.setStatus("current")
_Rcu52ConvGroups_ObjectIdentity = ObjectIdentity
rcu52ConvGroups = _Rcu52ConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 110)
)
_Rcu52ConvConformance_ObjectIdentity = ObjectIdentity
rcu52ConvConformance = _Rcu52ConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 111)
)

# Managed Objects groups

rcu52CNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 110, 1)
)
rcu52CNFReqGrp.setObjects(
      *(("PEAKRCU52-MIB", "rcu52Type"),
        ("PEAKRCU52-MIB", "rcu52SerialNo"),
        ("PEAKRCU52-MIB", "rcu52SoftwareVersion"),
        ("PEAKRCU52-MIB", "rcu52Remote"),
        ("PEAKRCU52-MIB", "rcu52AutoSwitch"),
        ("PEAKRCU52-MIB", "rcu52StandbyPosition"),
        ("PEAKRCU52-MIB", "rcu52UnitA"),
        ("PEAKRCU52-MIB", "rcu52UnitB"),
        ("PEAKRCU52-MIB", "rcu52UnitStandby"),
        ("PEAKRCU52-MIB", "rcu52SummaryAlarm"))
)
if mibBuilder.loadTexts:
    rcu52CNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rcu52CNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6025, 111, 1)
)
rcu52CNFCompliance.setObjects(
    ("PEAKRCU52-MIB", "rcu52CNFReqGrp")
)
if mibBuilder.loadTexts:
    rcu52CNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKRCU52-MIB",
    **{"Rcu52AutoSwType": Rcu52AutoSwType,
       "Rcu52StandbyPositionType": Rcu52StandbyPositionType,
       "peakRCU52Module": peakRCU52Module,
       "rcu52Type": rcu52Type,
       "rcu52SerialNo": rcu52SerialNo,
       "rcu52SoftwareVersion": rcu52SoftwareVersion,
       "rcu52Remote": rcu52Remote,
       "rcu52AutoSwitch": rcu52AutoSwitch,
       "rcu52StandbyPosition": rcu52StandbyPosition,
       "rcu52UnitA": rcu52UnitA,
       "rcu52UnitB": rcu52UnitB,
       "rcu52UnitStandby": rcu52UnitStandby,
       "rcu52SummaryAlarm": rcu52SummaryAlarm,
       "rcu52ConvGroups": rcu52ConvGroups,
       "rcu52CNFReqGrp": rcu52CNFReqGrp,
       "rcu52ConvConformance": rcu52ConvConformance,
       "rcu52CNFCompliance": rcu52CNFCompliance}
)
