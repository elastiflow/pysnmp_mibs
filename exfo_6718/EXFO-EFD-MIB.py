# SNMP MIB module (EXFO-EFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/EXFO-EFD-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(tmnEventObjectNotificationGroup,
 tmnEventStateNotificationGroup) = mibBuilder.importSymbols(
    "EXFO-EVENT-MIB",
    "tmnEventObjectNotificationGroup",
    "tmnEventStateNotificationGroup")

(exfoCommonMib,
 exfoModules) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoCommonMib",
    "exfoModules")

(AdministrativeState,
 OperationalState) = mibBuilder.importSymbols(
    "EXFO-TC",
    "AdministrativeState",
    "OperationalState")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

exfoEfdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventForwardingDiscriminator_ObjectIdentity = ObjectIdentity
eventForwardingDiscriminator = _EventForwardingDiscriminator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3)
)
if mibBuilder.loadTexts:
    eventForwardingDiscriminator.setStatus("current")
_EfdConf_ObjectIdentity = ObjectIdentity
efdConf = _EfdConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 1)
)
if mibBuilder.loadTexts:
    efdConf.setStatus("current")
_EfdGroups_ObjectIdentity = ObjectIdentity
efdGroups = _EfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    efdGroups.setStatus("current")
_EfdCompls_ObjectIdentity = ObjectIdentity
efdCompls = _EfdCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    efdCompls.setStatus("current")
_EfdObjs_ObjectIdentity = ObjectIdentity
efdObjs = _EfdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2)
)
if mibBuilder.loadTexts:
    efdObjs.setStatus("current")


class _EfdNextIndex_Type(Unsigned32):
    """Custom type efdNextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EfdNextIndex_Type.__name__ = "Unsigned32"
_EfdNextIndex_Object = MibScalar
efdNextIndex = _EfdNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 1),
    _EfdNextIndex_Type()
)
efdNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdNextIndex.setStatus("current")
_EfdTable_Object = MibTable
efdTable = _EfdTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    efdTable.setStatus("current")
_EfdEntry_Object = MibTableRow
efdEntry = _EfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 2, 1)
)
efdEntry.setIndexNames(
    (0, "EXFO-EFD-MIB", "efdIndex"),
)
if mibBuilder.loadTexts:
    efdEntry.setStatus("current")
_EfdIndex_Type = Unsigned32
_EfdIndex_Object = MibTableColumn
efdIndex = _EfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 2, 1, 1),
    _EfdIndex_Type()
)
efdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efdIndex.setStatus("current")
_EfdAdministrativeState_Type = AdministrativeState
_EfdAdministrativeState_Object = MibTableColumn
efdAdministrativeState = _EfdAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 2, 1, 2),
    _EfdAdministrativeState_Type()
)
efdAdministrativeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efdAdministrativeState.setStatus("current")
_EfdOperationalState_Type = OperationalState
_EfdOperationalState_Object = MibTableColumn
efdOperationalState = _EfdOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 2, 1, 3),
    _EfdOperationalState_Type()
)
efdOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdOperationalState.setStatus("current")
_EfdRowStatus_Type = RowStatus
_EfdRowStatus_Object = MibTableColumn
efdRowStatus = _EfdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 2, 2, 1, 4),
    _EfdRowStatus_Type()
)
efdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efdRowStatus.setStatus("current")
_EfdEvents_ObjectIdentity = ObjectIdentity
efdEvents = _EfdEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 3)
)
if mibBuilder.loadTexts:
    efdEvents.setStatus("current")

# Managed Objects groups

efdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 1, 1, 1)
)
efdGroup.setObjects(
      *(("EXFO-EFD-MIB", "efdNextIndex"),
        ("EXFO-EFD-MIB", "efdOperationalState"),
        ("EXFO-EFD-MIB", "efdAdministrativeState"),
        ("EXFO-EFD-MIB", "efdRowStatus"))
)
if mibBuilder.loadTexts:
    efdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

efdAdvancedCompls = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6718, 2, 3, 1, 2, 1)
)
efdAdvancedCompls.setObjects(
      *(("EXFO-EFD-MIB", "efdGroup"),
        ("EXFO-EFD-MIB", "tmnEventObjectNotificationGroup"),
        ("EXFO-EFD-MIB", "tmnEventStateNotificationGroup"))
)
if mibBuilder.loadTexts:
    efdAdvancedCompls.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXFO-EFD-MIB",
    **{"exfoEfdMib": exfoEfdMib,
       "eventForwardingDiscriminator": eventForwardingDiscriminator,
       "efdConf": efdConf,
       "efdGroups": efdGroups,
       "efdGroup": efdGroup,
       "efdCompls": efdCompls,
       "efdAdvancedCompls": efdAdvancedCompls,
       "efdObjs": efdObjs,
       "efdNextIndex": efdNextIndex,
       "efdTable": efdTable,
       "efdEntry": efdEntry,
       "efdIndex": efdIndex,
       "efdAdministrativeState": efdAdministrativeState,
       "efdOperationalState": efdOperationalState,
       "efdRowStatus": efdRowStatus,
       "efdEvents": efdEvents}
)
