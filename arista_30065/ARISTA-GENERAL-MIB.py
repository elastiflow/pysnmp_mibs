# SNMP MIB module (ARISTA-GENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-GENERAL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aristaGeneralMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24)
)
if mibBuilder.loadTexts:
    aristaGeneralMib.setRevisions(
        ("2017-11-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaGeneralMibNotifications_ObjectIdentity = ObjectIdentity
aristaGeneralMibNotifications = _AristaGeneralMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 0)
)
_AristaGeneralMibObjects_ObjectIdentity = ObjectIdentity
aristaGeneralMibObjects = _AristaGeneralMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1)
)
_AristaReloadCauseTable_Object = MibTable
aristaReloadCauseTable = _AristaReloadCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1)
)
if mibBuilder.loadTexts:
    aristaReloadCauseTable.setStatus("current")
_AristaReloadCauseEntry_Object = MibTableRow
aristaReloadCauseEntry = _AristaReloadCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1)
)
aristaReloadCauseEntry.setIndexNames(
    (0, "ARISTA-GENERAL-MIB", "aristaReloadUnitIndex"),
    (0, "ARISTA-GENERAL-MIB", "aristaReloadIndex"),
    (0, "ARISTA-GENERAL-MIB", "aristaReloadCauseIndex"),
)
if mibBuilder.loadTexts:
    aristaReloadCauseEntry.setStatus("current")
_AristaReloadUnitIndex_Type = Unsigned32
_AristaReloadUnitIndex_Object = MibTableColumn
aristaReloadUnitIndex = _AristaReloadUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 1),
    _AristaReloadUnitIndex_Type()
)
aristaReloadUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaReloadUnitIndex.setStatus("current")
_AristaReloadIndex_Type = Unsigned32
_AristaReloadIndex_Object = MibTableColumn
aristaReloadIndex = _AristaReloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 2),
    _AristaReloadIndex_Type()
)
aristaReloadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaReloadIndex.setStatus("current")
_AristaReloadCauseIndex_Type = Unsigned32
_AristaReloadCauseIndex_Object = MibTableColumn
aristaReloadCauseIndex = _AristaReloadCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 3),
    _AristaReloadCauseIndex_Type()
)
aristaReloadCauseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaReloadCauseIndex.setStatus("current")
_AristaReloadCauseDescription_Type = OctetString
_AristaReloadCauseDescription_Object = MibTableColumn
aristaReloadCauseDescription = _AristaReloadCauseDescription_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 4),
    _AristaReloadCauseDescription_Type()
)
aristaReloadCauseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaReloadCauseDescription.setStatus("current")
_AristaReloadTime_Type = DateAndTime
_AristaReloadTime_Object = MibTableColumn
aristaReloadTime = _AristaReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 5),
    _AristaReloadTime_Type()
)
aristaReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaReloadTime.setStatus("current")
_AristaGeneralMibConformance_ObjectIdentity = ObjectIdentity
aristaGeneralMibConformance = _AristaGeneralMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 2)
)
_AristaGeneralMibCompliances_ObjectIdentity = ObjectIdentity
aristaGeneralMibCompliances = _AristaGeneralMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 1)
)
_AristaGeneralMibGroups_ObjectIdentity = ObjectIdentity
aristaGeneralMibGroups = _AristaGeneralMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 2)
)

# Managed Objects groups

aristaGeneralMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 2, 1)
)
aristaGeneralMibGroup.setObjects(
      *(("ARISTA-GENERAL-MIB", "aristaReloadCauseDescription"),
        ("ARISTA-GENERAL-MIB", "aristaReloadTime"))
)
if mibBuilder.loadTexts:
    aristaGeneralMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaGeneralMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 1, 1)
)
aristaGeneralMibCompliance.setObjects(
    ("ARISTA-GENERAL-MIB", "aristaGeneralMibGroup")
)
if mibBuilder.loadTexts:
    aristaGeneralMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-GENERAL-MIB",
    **{"aristaGeneralMib": aristaGeneralMib,
       "aristaGeneralMibNotifications": aristaGeneralMibNotifications,
       "aristaGeneralMibObjects": aristaGeneralMibObjects,
       "aristaReloadCauseTable": aristaReloadCauseTable,
       "aristaReloadCauseEntry": aristaReloadCauseEntry,
       "aristaReloadUnitIndex": aristaReloadUnitIndex,
       "aristaReloadIndex": aristaReloadIndex,
       "aristaReloadCauseIndex": aristaReloadCauseIndex,
       "aristaReloadCauseDescription": aristaReloadCauseDescription,
       "aristaReloadTime": aristaReloadTime,
       "aristaGeneralMibConformance": aristaGeneralMibConformance,
       "aristaGeneralMibCompliances": aristaGeneralMibCompliances,
       "aristaGeneralMibCompliance": aristaGeneralMibCompliance,
       "aristaGeneralMibGroups": aristaGeneralMibGroups,
       "aristaGeneralMibGroup": aristaGeneralMibGroup}
)
