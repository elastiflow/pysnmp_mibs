# SNMP MIB module (INTEGRATED-SERVICES-GUARANTEED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/INTEGRATED-SERVICES-GUARANTEED-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:36:15 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(intSrv,) = mibBuilder.importSymbols(
    "INTEGRATED-SERVICES-MIB",
    "intSrv")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

intSrvGuaranteed = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 52, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IntSrvGuaranteedObjects_ObjectIdentity = ObjectIdentity
intSrvGuaranteedObjects = _IntSrvGuaranteedObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 5, 1)
)
_IntSrvGuaranteedIfTable_Object = MibTable
intSrvGuaranteedIfTable = _IntSrvGuaranteedIfTable_Object(
    (1, 3, 6, 1, 2, 1, 52, 5, 1, 1)
)
if mibBuilder.loadTexts:
    intSrvGuaranteedIfTable.setStatus("current")
_IntSrvGuaranteedIfEntry_Object = MibTableRow
intSrvGuaranteedIfEntry = _IntSrvGuaranteedIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1)
)
intSrvGuaranteedIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    intSrvGuaranteedIfEntry.setStatus("current")


class _IntSrvGuaranteedIfBacklog_Type(Integer32):
    """Custom type intSrvGuaranteedIfBacklog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_IntSrvGuaranteedIfBacklog_Type.__name__ = "Integer32"
_IntSrvGuaranteedIfBacklog_Object = MibTableColumn
intSrvGuaranteedIfBacklog = _IntSrvGuaranteedIfBacklog_Object(
    (1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 1),
    _IntSrvGuaranteedIfBacklog_Type()
)
intSrvGuaranteedIfBacklog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvGuaranteedIfBacklog.setStatus("current")
if mibBuilder.loadTexts:
    intSrvGuaranteedIfBacklog.setUnits("bytes")


class _IntSrvGuaranteedIfDelay_Type(Integer32):
    """Custom type intSrvGuaranteedIfDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_IntSrvGuaranteedIfDelay_Type.__name__ = "Integer32"
_IntSrvGuaranteedIfDelay_Object = MibTableColumn
intSrvGuaranteedIfDelay = _IntSrvGuaranteedIfDelay_Object(
    (1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 2),
    _IntSrvGuaranteedIfDelay_Type()
)
intSrvGuaranteedIfDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvGuaranteedIfDelay.setStatus("current")
if mibBuilder.loadTexts:
    intSrvGuaranteedIfDelay.setUnits("microseconds")


class _IntSrvGuaranteedIfSlack_Type(Integer32):
    """Custom type intSrvGuaranteedIfSlack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_IntSrvGuaranteedIfSlack_Type.__name__ = "Integer32"
_IntSrvGuaranteedIfSlack_Object = MibTableColumn
intSrvGuaranteedIfSlack = _IntSrvGuaranteedIfSlack_Object(
    (1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 3),
    _IntSrvGuaranteedIfSlack_Type()
)
intSrvGuaranteedIfSlack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvGuaranteedIfSlack.setStatus("current")
_IntSrvGuaranteedIfStatus_Type = RowStatus
_IntSrvGuaranteedIfStatus_Object = MibTableColumn
intSrvGuaranteedIfStatus = _IntSrvGuaranteedIfStatus_Object(
    (1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 4),
    _IntSrvGuaranteedIfStatus_Type()
)
intSrvGuaranteedIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    intSrvGuaranteedIfStatus.setStatus("current")
_IntSrvGuaranteedNotifications_ObjectIdentity = ObjectIdentity
intSrvGuaranteedNotifications = _IntSrvGuaranteedNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 5, 2)
)
_IntSrvGuaranteedConformance_ObjectIdentity = ObjectIdentity
intSrvGuaranteedConformance = _IntSrvGuaranteedConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 5, 3)
)
_IntSrvGuaranteedGroups_ObjectIdentity = ObjectIdentity
intSrvGuaranteedGroups = _IntSrvGuaranteedGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 5, 3, 1)
)
_IntSrvGuaranteedCompliances_ObjectIdentity = ObjectIdentity
intSrvGuaranteedCompliances = _IntSrvGuaranteedCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 52, 5, 3, 2)
)

# Managed Objects groups

intSrvGuaranteedIfAttribGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 52, 5, 3, 1, 2)
)
intSrvGuaranteedIfAttribGroup.setObjects(
      *(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfBacklog"),
        ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfDelay"),
        ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"),
        ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"))
)
if mibBuilder.loadTexts:
    intSrvGuaranteedIfAttribGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

intSrvGuaranteedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 52, 5, 3, 2, 1)
)
intSrvGuaranteedCompliance.setObjects(
    ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup")
)
if mibBuilder.loadTexts:
    intSrvGuaranteedCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEGRATED-SERVICES-GUARANTEED-MIB",
    **{"intSrvGuaranteed": intSrvGuaranteed,
       "intSrvGuaranteedObjects": intSrvGuaranteedObjects,
       "intSrvGuaranteedIfTable": intSrvGuaranteedIfTable,
       "intSrvGuaranteedIfEntry": intSrvGuaranteedIfEntry,
       "intSrvGuaranteedIfBacklog": intSrvGuaranteedIfBacklog,
       "intSrvGuaranteedIfDelay": intSrvGuaranteedIfDelay,
       "intSrvGuaranteedIfSlack": intSrvGuaranteedIfSlack,
       "intSrvGuaranteedIfStatus": intSrvGuaranteedIfStatus,
       "intSrvGuaranteedNotifications": intSrvGuaranteedNotifications,
       "intSrvGuaranteedConformance": intSrvGuaranteedConformance,
       "intSrvGuaranteedGroups": intSrvGuaranteedGroups,
       "intSrvGuaranteedIfAttribGroup": intSrvGuaranteedIfAttribGroup,
       "intSrvGuaranteedCompliances": intSrvGuaranteedCompliances,
       "intSrvGuaranteedCompliance": intSrvGuaranteedCompliance}
)
