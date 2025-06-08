# SNMP MIB module (CISCO-CAT6k-NAT-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CAT6k-NAT-STAT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:49:42 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoCat6kNatStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 861)
)
if mibBuilder.loadTexts:
    ciscoCat6kNatStatMIB.setRevisions(
        ("2019-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NatType(TextualConvention, Integer32):
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
        *(("static", 1),
          ("dynamic", 2),
          ("mixed", 3),
          ("other", 4))
    )



class NetFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 1),
          ("mixed", 2))
    )



class NatBool(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCat6kNatStatMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCat6kNatStatMIBObjects = _CiscoCat6kNatStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1)
)
_CiscoCat6kNatStatus_ObjectIdentity = ObjectIdentity
ciscoCat6kNatStatus = _CiscoCat6kNatStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2)
)
_CiscoCat6kNatType_Type = NatType
_CiscoCat6kNatType_Object = MibScalar
ciscoCat6kNatType = _CiscoCat6kNatType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 1),
    _CiscoCat6kNatType_Type()
)
ciscoCat6kNatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatType.setStatus("current")
_CiscoCat6kNatNetFlowType_Type = NetFlowType
_CiscoCat6kNatNetFlowType_Object = MibScalar
ciscoCat6kNatNetFlowType = _CiscoCat6kNatNetFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 2),
    _CiscoCat6kNatNetFlowType_Type()
)
ciscoCat6kNatNetFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatNetFlowType.setStatus("current")
_CiscoCat6kNatFlowRecord_Type = NatBool
_CiscoCat6kNatFlowRecord_Object = MibScalar
ciscoCat6kNatFlowRecord = _CiscoCat6kNatFlowRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 3),
    _CiscoCat6kNatFlowRecord_Type()
)
ciscoCat6kNatFlowRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatFlowRecord.setStatus("current")
_CiscoCat6kNatDynamicEntryUtilization_Type = OctetString
_CiscoCat6kNatDynamicEntryUtilization_Object = MibScalar
ciscoCat6kNatDynamicEntryUtilization = _CiscoCat6kNatDynamicEntryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 4),
    _CiscoCat6kNatDynamicEntryUtilization_Type()
)
ciscoCat6kNatDynamicEntryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatDynamicEntryUtilization.setStatus("current")
_CiscoCat6kNatStaticEntryUtilization_Type = OctetString
_CiscoCat6kNatStaticEntryUtilization_Object = MibScalar
ciscoCat6kNatStaticEntryUtilization = _CiscoCat6kNatStaticEntryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 5),
    _CiscoCat6kNatStaticEntryUtilization_Type()
)
ciscoCat6kNatStaticEntryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatStaticEntryUtilization.setStatus("current")
_CiscoCat6kNatOtherEntryUtilization_Type = OctetString
_CiscoCat6kNatOtherEntryUtilization_Object = MibScalar
ciscoCat6kNatOtherEntryUtilization = _CiscoCat6kNatOtherEntryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 6),
    _CiscoCat6kNatOtherEntryUtilization_Type()
)
ciscoCat6kNatOtherEntryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatOtherEntryUtilization.setStatus("current")
_CiscoCat6kNatTotalEntryCount_Type = Counter32
_CiscoCat6kNatTotalEntryCount_Object = MibScalar
ciscoCat6kNatTotalEntryCount = _CiscoCat6kNatTotalEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 7),
    _CiscoCat6kNatTotalEntryCount_Type()
)
ciscoCat6kNatTotalEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatTotalEntryCount.setStatus("current")
_CiscoCat6kNatResourceUtilization_Type = OctetString
_CiscoCat6kNatResourceUtilization_Object = MibScalar
ciscoCat6kNatResourceUtilization = _CiscoCat6kNatResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 8),
    _CiscoCat6kNatResourceUtilization_Type()
)
ciscoCat6kNatResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCat6kNatResourceUtilization.setStatus("current")
_CiscoCat6kNatStatMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCat6kNatStatMIBConformance = _CiscoCat6kNatStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 2)
)
_CiscoCat6kNatStatMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCat6kNatStatMIBCompliances = _CiscoCat6kNatStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 1)
)
_CiscoCat6kNatStatMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCat6kNatStatMIBGroups = _CiscoCat6kNatStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 2)
)

# Managed Objects groups

ciscoCat6kNatStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 2, 1)
)
ciscoCat6kNatStatGroup.setObjects(
      *(("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatType"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatNetFlowType"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatFlowRecord"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatDynamicEntryUtilization"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatStaticEntryUtilization"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatOtherEntryUtilization"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatTotalEntryCount"),
        ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatResourceUtilization"))
)
if mibBuilder.loadTexts:
    ciscoCat6kNatStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCat6kNatStatMIBComplianceVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 1, 1)
)
ciscoCat6kNatStatMIBComplianceVer1.setObjects(
    ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatStatGroup")
)
if mibBuilder.loadTexts:
    ciscoCat6kNatStatMIBComplianceVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAT6k-NAT-STAT-MIB",
    **{"NatType": NatType,
       "NetFlowType": NetFlowType,
       "NatBool": NatBool,
       "ciscoCat6kNatStatMIB": ciscoCat6kNatStatMIB,
       "ciscoCat6kNatStatMIBObjects": ciscoCat6kNatStatMIBObjects,
       "ciscoCat6kNatStatus": ciscoCat6kNatStatus,
       "ciscoCat6kNatType": ciscoCat6kNatType,
       "ciscoCat6kNatNetFlowType": ciscoCat6kNatNetFlowType,
       "ciscoCat6kNatFlowRecord": ciscoCat6kNatFlowRecord,
       "ciscoCat6kNatDynamicEntryUtilization": ciscoCat6kNatDynamicEntryUtilization,
       "ciscoCat6kNatStaticEntryUtilization": ciscoCat6kNatStaticEntryUtilization,
       "ciscoCat6kNatOtherEntryUtilization": ciscoCat6kNatOtherEntryUtilization,
       "ciscoCat6kNatTotalEntryCount": ciscoCat6kNatTotalEntryCount,
       "ciscoCat6kNatResourceUtilization": ciscoCat6kNatResourceUtilization,
       "ciscoCat6kNatStatMIBConformance": ciscoCat6kNatStatMIBConformance,
       "ciscoCat6kNatStatMIBCompliances": ciscoCat6kNatStatMIBCompliances,
       "ciscoCat6kNatStatMIBComplianceVer1": ciscoCat6kNatStatMIBComplianceVer1,
       "ciscoCat6kNatStatMIBGroups": ciscoCat6kNatStatMIBGroups,
       "ciscoCat6kNatStatGroup": ciscoCat6kNatStatGroup}
)
