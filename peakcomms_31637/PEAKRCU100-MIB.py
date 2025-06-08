# SNMP MIB module (PEAKRCU100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKRCU100-MIB.mib
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

peakRCU100Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001)
)
if mibBuilder.loadTexts:
    peakRCU100Module.setRevisions(
        ("2015-09-15 10:00",
         "2013-04-04 12:00",
         "2010-08-04 12:00",
         "2010-06-17 09:00",
         "2010-05-27 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rcu100AutoSwType(TextualConvention, Integer32):
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



class Rcu100BandType(TextualConvention, Integer32):
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
          ("unitB", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Rcu100Type_Type = OctetString
_Rcu100Type_Object = MibScalar
rcu100Type = _Rcu100Type_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 1),
    _Rcu100Type_Type()
)
rcu100Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100Type.setStatus("current")


class _Rcu100SerialNo_Type(Integer32):
    """Custom type rcu100SerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rcu100SerialNo_Type.__name__ = "Integer32"
_Rcu100SerialNo_Object = MibScalar
rcu100SerialNo = _Rcu100SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 2),
    _Rcu100SerialNo_Type()
)
rcu100SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100SerialNo.setStatus("current")
_Rcu100SoftwareVersion_Type = OctetString
_Rcu100SoftwareVersion_Object = MibScalar
rcu100SoftwareVersion = _Rcu100SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 3),
    _Rcu100SoftwareVersion_Type()
)
rcu100SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100SoftwareVersion.setStatus("current")
_Rcu100Remote_Type = RemoteLocalType
_Rcu100Remote_Object = MibScalar
rcu100Remote = _Rcu100Remote_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 4),
    _Rcu100Remote_Type()
)
rcu100Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100Remote.setStatus("current")
_Rcu100AutoSwitch_Type = Rcu100AutoSwType
_Rcu100AutoSwitch_Object = MibScalar
rcu100AutoSwitch = _Rcu100AutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 5),
    _Rcu100AutoSwitch_Type()
)
rcu100AutoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu100AutoSwitch.setStatus("current")
_Rcu100Band_Type = Rcu100BandType
_Rcu100Band_Object = MibScalar
rcu100Band = _Rcu100Band_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 6),
    _Rcu100Band_Type()
)
rcu100Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100Band.setStatus("current")
_Rcu100UnitA_Type = OnOffType
_Rcu100UnitA_Object = MibScalar
rcu100UnitA = _Rcu100UnitA_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 7),
    _Rcu100UnitA_Type()
)
rcu100UnitA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100UnitA.setStatus("current")
_Rcu100UnitB_Type = OnOffType
_Rcu100UnitB_Object = MibScalar
rcu100UnitB = _Rcu100UnitB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 8),
    _Rcu100UnitB_Type()
)
rcu100UnitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100UnitB.setStatus("current")
_Rcu100SummaryAlarm_Type = FaultType
_Rcu100SummaryAlarm_Object = MibScalar
rcu100SummaryAlarm = _Rcu100SummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 9),
    _Rcu100SummaryAlarm_Type()
)
rcu100SummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu100SummaryAlarm.setStatus("current")
_Rcu100ConvGroups_ObjectIdentity = ObjectIdentity
rcu100ConvGroups = _Rcu100ConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 110)
)
_Rcu100ConvConformance_ObjectIdentity = ObjectIdentity
rcu100ConvConformance = _Rcu100ConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 111)
)

# Managed Objects groups

rcu100CNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 110, 1)
)
rcu100CNFReqGrp.setObjects(
      *(("PEAKRCU100-MIB", "rcu100Type"),
        ("PEAKRCU100-MIB", "rcu100SerialNo"),
        ("PEAKRCU100-MIB", "rcu100SoftwareVersion"),
        ("PEAKRCU100-MIB", "rcu100Remote"),
        ("PEAKRCU100-MIB", "rcu100AutoSwitch"),
        ("PEAKRCU100-MIB", "rcu100Band"),
        ("PEAKRCU100-MIB", "rcu100UnitA"),
        ("PEAKRCU100-MIB", "rcu100UnitB"),
        ("PEAKRCU100-MIB", "rcu100SummaryAlarm"))
)
if mibBuilder.loadTexts:
    rcu100CNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rcu100CNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6001, 111, 1)
)
rcu100CNFCompliance.setObjects(
    ("PEAKRCU100-MIB", "rcu100CNFReqGrp")
)
if mibBuilder.loadTexts:
    rcu100CNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKRCU100-MIB",
    **{"Rcu100AutoSwType": Rcu100AutoSwType,
       "Rcu100BandType": Rcu100BandType,
       "peakRCU100Module": peakRCU100Module,
       "rcu100Type": rcu100Type,
       "rcu100SerialNo": rcu100SerialNo,
       "rcu100SoftwareVersion": rcu100SoftwareVersion,
       "rcu100Remote": rcu100Remote,
       "rcu100AutoSwitch": rcu100AutoSwitch,
       "rcu100Band": rcu100Band,
       "rcu100UnitA": rcu100UnitA,
       "rcu100UnitB": rcu100UnitB,
       "rcu100SummaryAlarm": rcu100SummaryAlarm,
       "rcu100ConvGroups": rcu100ConvGroups,
       "rcu100CNFReqGrp": rcu100CNFReqGrp,
       "rcu100ConvConformance": rcu100ConvConformance,
       "rcu100CNFCompliance": rcu100CNFCompliance}
)
