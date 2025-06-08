# SNMP MIB module (CISCO-IETF-MPLS-ID-STD-03-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IETF-MPLS-ID-STD-03-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:29:56 2025
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

(CMplsGlobalId,
 CMplsIccId,
 CMplsNodeId) = mibBuilder.importSymbols(
    "CISCO-MPLS-TC-EXT-STD-MIB",
    "CMplsGlobalId",
    "CMplsIccId",
    "CMplsNodeId")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

cmplsIdStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 147)
)
if mibBuilder.loadTexts:
    cmplsIdStdMIB.setRevisions(
        ("2012-04-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmplsIdNotifications_ObjectIdentity = ObjectIdentity
cmplsIdNotifications = _CmplsIdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 0)
)
_CmplsIdObjects_ObjectIdentity = ObjectIdentity
cmplsIdObjects = _CmplsIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 1)
)
_CmplsGlobalId_Type = CMplsGlobalId
_CmplsGlobalId_Object = MibScalar
cmplsGlobalId = _CmplsGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 1),
    _CmplsGlobalId_Type()
)
cmplsGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsGlobalId.setStatus("current")
_CmplsIcc_Type = CMplsIccId
_CmplsIcc_Object = MibScalar
cmplsIcc = _CmplsIcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 2),
    _CmplsIcc_Type()
)
cmplsIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsIcc.setStatus("current")
_CmplsNodeId_Type = CMplsNodeId
_CmplsNodeId_Object = MibScalar
cmplsNodeId = _CmplsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 3),
    _CmplsNodeId_Type()
)
cmplsNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsNodeId.setStatus("current")
_CmplsIdConformance_ObjectIdentity = ObjectIdentity
cmplsIdConformance = _CmplsIdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 2)
)
_CmplsIdGroups_ObjectIdentity = ObjectIdentity
cmplsIdGroups = _CmplsIdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1)
)
_CmplsIdCompliances_ObjectIdentity = ObjectIdentity
cmplsIdCompliances = _CmplsIdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2)
)

# Managed Objects groups

cmplsIdScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1, 1)
)
cmplsIdScalarGroup.setObjects(
      *(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsGlobalId"),
        ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsNodeId"),
        ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIcc"))
)
if mibBuilder.loadTexts:
    cmplsIdScalarGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmplsIdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 1)
)
cmplsIdModuleFullCompliance.setObjects(
    ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup")
)
if mibBuilder.loadTexts:
    cmplsIdModuleFullCompliance.setStatus(
        "current"
    )

cmplsIdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 2)
)
cmplsIdModuleReadOnlyCompliance.setObjects(
    ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup")
)
if mibBuilder.loadTexts:
    cmplsIdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-MPLS-ID-STD-03-MIB",
    **{"cmplsIdStdMIB": cmplsIdStdMIB,
       "cmplsIdNotifications": cmplsIdNotifications,
       "cmplsIdObjects": cmplsIdObjects,
       "cmplsGlobalId": cmplsGlobalId,
       "cmplsIcc": cmplsIcc,
       "cmplsNodeId": cmplsNodeId,
       "cmplsIdConformance": cmplsIdConformance,
       "cmplsIdGroups": cmplsIdGroups,
       "cmplsIdScalarGroup": cmplsIdScalarGroup,
       "cmplsIdCompliances": cmplsIdCompliances,
       "cmplsIdModuleFullCompliance": cmplsIdModuleFullCompliance,
       "cmplsIdModuleReadOnlyCompliance": cmplsIdModuleReadOnlyCompliance}
)
