# SNMP MIB module (CISCO-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-QOS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:37 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100)
)
if mibBuilder.loadTexts:
    ciscoQoSMIB.setRevisions(
        ("1998-02-26 00:00",
         "1998-02-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoQoSPrecedence(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class CiscoWrrSchedWeight(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoQoSMIBObjects_ObjectIdentity = ObjectIdentity
ciscoQoSMIBObjects = _CiscoQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1)
)
_CiscoQoSControl_ObjectIdentity = ObjectIdentity
ciscoQoSControl = _CiscoQoSControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 1)
)


class _CiscoQoSEnable_Type(TruthValue):
    """Custom type ciscoQoSEnable based on TruthValue"""
    defaultValue = 1


_CiscoQoSEnable_Type.__name__ = "TruthValue"
_CiscoQoSEnable_Object = MibScalar
ciscoQoSEnable = _CiscoQoSEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 1, 1),
    _CiscoQoSEnable_Type()
)
ciscoQoSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoQoSEnable.setStatus("current")
_CiscoQoSMap_ObjectIdentity = ObjectIdentity
ciscoQoSMap = _CiscoQoSMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2)
)
_CiscoQoSMapTable_Object = MibTable
ciscoQoSMapTable = _CiscoQoSMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoQoSMapTable.setStatus("current")
_CiscoQoSMapEntry_Object = MibTableRow
ciscoQoSMapEntry = _CiscoQoSMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1, 1)
)
ciscoQoSMapEntry.setIndexNames(
    (0, "CISCO-QOS-MIB", "ciscoQoSMapSrcIf"),
    (0, "CISCO-QOS-MIB", "ciscoQoSMapDstIf"),
    (0, "CISCO-QOS-MIB", "ciscoQoSMapPrecedence"),
)
if mibBuilder.loadTexts:
    ciscoQoSMapEntry.setStatus("current")
_CiscoQoSMapSrcIf_Type = InterfaceIndexOrZero
_CiscoQoSMapSrcIf_Object = MibTableColumn
ciscoQoSMapSrcIf = _CiscoQoSMapSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1, 1, 1),
    _CiscoQoSMapSrcIf_Type()
)
ciscoQoSMapSrcIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoQoSMapSrcIf.setStatus("current")
_CiscoQoSMapDstIf_Type = InterfaceIndexOrZero
_CiscoQoSMapDstIf_Object = MibTableColumn
ciscoQoSMapDstIf = _CiscoQoSMapDstIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1, 1, 2),
    _CiscoQoSMapDstIf_Type()
)
ciscoQoSMapDstIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoQoSMapDstIf.setStatus("current")
_CiscoQoSMapPrecedence_Type = CiscoQoSPrecedence
_CiscoQoSMapPrecedence_Object = MibTableColumn
ciscoQoSMapPrecedence = _CiscoQoSMapPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1, 1, 3),
    _CiscoQoSMapPrecedence_Type()
)
ciscoQoSMapPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoQoSMapPrecedence.setStatus("current")
_CiscoQoSMapWrrWeight_Type = CiscoWrrSchedWeight
_CiscoQoSMapWrrWeight_Object = MibTableColumn
ciscoQoSMapWrrWeight = _CiscoQoSMapWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1, 1, 4),
    _CiscoQoSMapWrrWeight_Type()
)
ciscoQoSMapWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoQoSMapWrrWeight.setStatus("current")


class _CiscoQoSMapRowStatus_Type(RowStatus):
    """Custom type ciscoQoSMapRowStatus based on RowStatus"""
    defaultValue = 1


_CiscoQoSMapRowStatus_Type.__name__ = "RowStatus"
_CiscoQoSMapRowStatus_Object = MibTableColumn
ciscoQoSMapRowStatus = _CiscoQoSMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 1, 2, 1, 1, 5),
    _CiscoQoSMapRowStatus_Type()
)
ciscoQoSMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoQoSMapRowStatus.setStatus("current")
_CiscoQoSMIBConformance_ObjectIdentity = ObjectIdentity
ciscoQoSMIBConformance = _CiscoQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 3)
)
_CiscoQoSMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoQoSMIBCompliances = _CiscoQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 3, 1)
)
_CiscoQoSMIBGroups_ObjectIdentity = ObjectIdentity
ciscoQoSMIBGroups = _CiscoQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 3, 2)
)

# Managed Objects groups

ciscoQoSMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 3, 2, 1)
)
ciscoQoSMIBGroup.setObjects(
      *(("CISCO-QOS-MIB", "ciscoQoSEnable"),
        ("CISCO-QOS-MIB", "ciscoQoSMapSrcIf"),
        ("CISCO-QOS-MIB", "ciscoQoSMapDstIf"),
        ("CISCO-QOS-MIB", "ciscoQoSMapPrecedence"),
        ("CISCO-QOS-MIB", "ciscoQoSMapWrrWeight"),
        ("CISCO-QOS-MIB", "ciscoQoSMapRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoQoSMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 100, 3, 1, 1)
)
ciscoQoSMIBCompliance.setObjects(
    ("CISCO-QOS-MIB", "ciscoQoSMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QOS-MIB",
    **{"CiscoQoSPrecedence": CiscoQoSPrecedence,
       "CiscoWrrSchedWeight": CiscoWrrSchedWeight,
       "ciscoQoSMIB": ciscoQoSMIB,
       "ciscoQoSMIBObjects": ciscoQoSMIBObjects,
       "ciscoQoSControl": ciscoQoSControl,
       "ciscoQoSEnable": ciscoQoSEnable,
       "ciscoQoSMap": ciscoQoSMap,
       "ciscoQoSMapTable": ciscoQoSMapTable,
       "ciscoQoSMapEntry": ciscoQoSMapEntry,
       "ciscoQoSMapSrcIf": ciscoQoSMapSrcIf,
       "ciscoQoSMapDstIf": ciscoQoSMapDstIf,
       "ciscoQoSMapPrecedence": ciscoQoSMapPrecedence,
       "ciscoQoSMapWrrWeight": ciscoQoSMapWrrWeight,
       "ciscoQoSMapRowStatus": ciscoQoSMapRowStatus,
       "ciscoQoSMIBConformance": ciscoQoSMIBConformance,
       "ciscoQoSMIBCompliances": ciscoQoSMIBCompliances,
       "ciscoQoSMIBCompliance": ciscoQoSMIBCompliance,
       "ciscoQoSMIBGroups": ciscoQoSMIBGroups,
       "ciscoQoSMIBGroup": ciscoQoSMIBGroup}
)
