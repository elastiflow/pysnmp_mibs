# SNMP MIB module (MPLS-ID-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/MPLS-ID-STD-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:44:43 2025
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

(MplsCcId,
 MplsGlobalId,
 MplsIccId,
 MplsNodeId) = mibBuilder.importSymbols(
    "MPLS-TC-EXT-STD-MIB",
    "MplsCcId",
    "MplsGlobalId",
    "MplsIccId",
    "MplsNodeId")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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

mplsIdStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 18)
)
if mibBuilder.loadTexts:
    mplsIdStdMIB.setRevisions(
        ("2015-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsIdNotifications_ObjectIdentity = ObjectIdentity
mplsIdNotifications = _MplsIdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 0)
)
_MplsIdObjects_ObjectIdentity = ObjectIdentity
mplsIdObjects = _MplsIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 1)
)
_MplsIdGlobalId_Type = MplsGlobalId
_MplsIdGlobalId_Object = MibScalar
mplsIdGlobalId = _MplsIdGlobalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 1),
    _MplsIdGlobalId_Type()
)
mplsIdGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIdGlobalId.setStatus("current")
_MplsIdNodeId_Type = MplsNodeId
_MplsIdNodeId_Object = MibScalar
mplsIdNodeId = _MplsIdNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 2),
    _MplsIdNodeId_Type()
)
mplsIdNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIdNodeId.setStatus("current")
_MplsIdCc_Type = MplsCcId
_MplsIdCc_Object = MibScalar
mplsIdCc = _MplsIdCc_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 3),
    _MplsIdCc_Type()
)
mplsIdCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIdCc.setStatus("current")
_MplsIdIcc_Type = MplsIccId
_MplsIdIcc_Object = MibScalar
mplsIdIcc = _MplsIdIcc_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 4),
    _MplsIdIcc_Type()
)
mplsIdIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsIdIcc.setStatus("current")
_MplsIdConformance_ObjectIdentity = ObjectIdentity
mplsIdConformance = _MplsIdConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2)
)
_MplsIdCompliances_ObjectIdentity = ObjectIdentity
mplsIdCompliances = _MplsIdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1)
)
_MplsIdGroups_ObjectIdentity = ObjectIdentity
mplsIdGroups = _MplsIdGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2)
)

# Managed Objects groups

mplsIdIpOperatorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 1)
)
mplsIdIpOperatorGroup.setObjects(
      *(("MPLS-ID-STD-MIB", "mplsIdGlobalId"),
        ("MPLS-ID-STD-MIB", "mplsIdNodeId"))
)
if mibBuilder.loadTexts:
    mplsIdIpOperatorGroup.setStatus("current")

mplsIdIccOperatorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 2)
)
mplsIdIccOperatorGroup.setObjects(
      *(("MPLS-ID-STD-MIB", "mplsIdNodeId"),
        ("MPLS-ID-STD-MIB", "mplsIdCc"),
        ("MPLS-ID-STD-MIB", "mplsIdIcc"))
)
if mibBuilder.loadTexts:
    mplsIdIccOperatorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsIdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 1)
)
mplsIdModuleFullCompliance.setObjects(
      *(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"),
        ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))
)
if mibBuilder.loadTexts:
    mplsIdModuleFullCompliance.setStatus(
        "current"
    )

mplsIdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 2)
)
mplsIdModuleReadOnlyCompliance.setObjects(
      *(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"),
        ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))
)
if mibBuilder.loadTexts:
    mplsIdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-ID-STD-MIB",
    **{"mplsIdStdMIB": mplsIdStdMIB,
       "mplsIdNotifications": mplsIdNotifications,
       "mplsIdObjects": mplsIdObjects,
       "mplsIdGlobalId": mplsIdGlobalId,
       "mplsIdNodeId": mplsIdNodeId,
       "mplsIdCc": mplsIdCc,
       "mplsIdIcc": mplsIdIcc,
       "mplsIdConformance": mplsIdConformance,
       "mplsIdCompliances": mplsIdCompliances,
       "mplsIdModuleFullCompliance": mplsIdModuleFullCompliance,
       "mplsIdModuleReadOnlyCompliance": mplsIdModuleReadOnlyCompliance,
       "mplsIdGroups": mplsIdGroups,
       "mplsIdIpOperatorGroup": mplsIdIpOperatorGroup,
       "mplsIdIccOperatorGroup": mplsIdIccOperatorGroup}
)
