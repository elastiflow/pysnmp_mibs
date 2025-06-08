# SNMP MIB module (CISCO-MPLS-LSR-EXT-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MPLS-LSR-EXT-STD-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:36 2025
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

(mplsInSegmentGroup,
 mplsLsrNotificationGroup,
 mplsOutSegmentGroup,
 mplsPerfGroup,
 mplsXCGroup,
 mplsXCInSegmentIndex,
 mplsXCIndex,
 mplsXCOutSegmentIndex) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsInSegmentGroup",
    "mplsLsrNotificationGroup",
    "mplsOutSegmentGroup",
    "mplsPerfGroup",
    "mplsXCGroup",
    "mplsXCInSegmentIndex",
    "mplsXCIndex",
    "mplsXCOutSegmentIndex")

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
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

cmplsLsrExtStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 145)
)
if mibBuilder.loadTexts:
    cmplsLsrExtStdMIB.setRevisions(
        ("2012-02-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmplsLsrExtNotifications_ObjectIdentity = ObjectIdentity
cmplsLsrExtNotifications = _CmplsLsrExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 0)
)
_CmplsLsrExtObjects_ObjectIdentity = ObjectIdentity
cmplsLsrExtObjects = _CmplsLsrExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 1)
)
_CmplsXCExtTable_Object = MibTable
cmplsXCExtTable = _CmplsXCExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1)
)
if mibBuilder.loadTexts:
    cmplsXCExtTable.setStatus("current")
_CmplsXCExtEntry_Object = MibTableRow
cmplsXCExtEntry = _CmplsXCExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1)
)
cmplsXCExtEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsXCIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"),
    (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    cmplsXCExtEntry.setStatus("current")
_CmplsXCExtTunnelPointer_Type = RowPointer
_CmplsXCExtTunnelPointer_Object = MibTableColumn
cmplsXCExtTunnelPointer = _CmplsXCExtTunnelPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 1),
    _CmplsXCExtTunnelPointer_Type()
)
cmplsXCExtTunnelPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsXCExtTunnelPointer.setStatus("current")
_CmplsXCOppositeDirXCPtr_Type = RowPointer
_CmplsXCOppositeDirXCPtr_Object = MibTableColumn
cmplsXCOppositeDirXCPtr = _CmplsXCOppositeDirXCPtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 2),
    _CmplsXCOppositeDirXCPtr_Type()
)
cmplsXCOppositeDirXCPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsXCOppositeDirXCPtr.setStatus("current")
_CmplsLsrExtConformance_ObjectIdentity = ObjectIdentity
cmplsLsrExtConformance = _CmplsLsrExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 2)
)
_CmplsLsrExtGroups_ObjectIdentity = ObjectIdentity
cmplsLsrExtGroups = _CmplsLsrExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1)
)
_CmplsLsrExtCompliances_ObjectIdentity = ObjectIdentity
cmplsLsrExtCompliances = _CmplsLsrExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2)
)

# Managed Objects groups

cmplsXCExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1, 1)
)
cmplsXCExtGroup.setObjects(
      *(("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtTunnelPointer"),
        ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCOppositeDirXCPtr"))
)
if mibBuilder.loadTexts:
    cmplsXCExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmplsLsrExtModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 1)
)
cmplsLsrExtModuleFullCompliance.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsXCGroup"),
        ("MPLS-LSR-STD-MIB", "mplsPerfGroup"),
        ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"),
        ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))
)
if mibBuilder.loadTexts:
    cmplsLsrExtModuleFullCompliance.setStatus(
        "current"
    )

cmplsLsrExtModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 2)
)
cmplsLsrExtModuleReadOnlyCompliance.setObjects(
      *(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsXCGroup"),
        ("MPLS-LSR-STD-MIB", "mplsPerfGroup"),
        ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))
)
if mibBuilder.loadTexts:
    cmplsLsrExtModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MPLS-LSR-EXT-STD-MIB",
    **{"cmplsLsrExtStdMIB": cmplsLsrExtStdMIB,
       "cmplsLsrExtNotifications": cmplsLsrExtNotifications,
       "cmplsLsrExtObjects": cmplsLsrExtObjects,
       "cmplsXCExtTable": cmplsXCExtTable,
       "cmplsXCExtEntry": cmplsXCExtEntry,
       "cmplsXCExtTunnelPointer": cmplsXCExtTunnelPointer,
       "cmplsXCOppositeDirXCPtr": cmplsXCOppositeDirXCPtr,
       "cmplsLsrExtConformance": cmplsLsrExtConformance,
       "cmplsLsrExtGroups": cmplsLsrExtGroups,
       "cmplsXCExtGroup": cmplsXCExtGroup,
       "cmplsLsrExtCompliances": cmplsLsrExtCompliances,
       "cmplsLsrExtModuleFullCompliance": cmplsLsrExtModuleFullCompliance,
       "cmplsLsrExtModuleReadOnlyCompliance": cmplsLsrExtModuleReadOnlyCompliance}
)
