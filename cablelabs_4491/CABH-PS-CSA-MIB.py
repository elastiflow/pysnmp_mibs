# SNMP MIB module (CABH-PS-CSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CABH-PS-CSA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:05 2025
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

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(rip2IfStatEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfStatEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cabhPsCsaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhPsCsaNotifications_ObjectIdentity = ObjectIdentity
cabhPsCsaNotifications = _CabhPsCsaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 0)
)
_CabhPsCsaMibObjects_ObjectIdentity = ObjectIdentity
cabhPsCsaMibObjects = _CabhPsCsaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1)
)
_CabhPsDevCsaObjects_ObjectIdentity = ObjectIdentity
cabhPsDevCsaObjects = _CabhPsDevCsaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 1)
)
_CabhPsDevCsaRipExtension_ObjectIdentity = ObjectIdentity
cabhPsDevCsaRipExtension = _CabhPsDevCsaRipExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 1, 1)
)
_CabhPsDevCsaRip2IfConfExtTable_Object = MibTable
cabhPsDevCsaRip2IfConfExtTable = _CabhPsDevCsaRip2IfConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cabhPsDevCsaRip2IfConfExtTable.setStatus("current")
_CabhPsDevCsaRip2IfConfExtEntry_Object = MibTableRow
cabhPsDevCsaRip2IfConfExtEntry = _CabhPsDevCsaRip2IfConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cabhPsDevCsaRip2IfConfExtEntry.setStatus("current")


class _CabhPsDevCsaRip2IfConfAuthKeyId_Type(Unsigned32):
    """Custom type cabhPsDevCsaRip2IfConfAuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CabhPsDevCsaRip2IfConfAuthKeyId_Type.__name__ = "Unsigned32"
_CabhPsDevCsaRip2IfConfAuthKeyId_Object = MibTableColumn
cabhPsDevCsaRip2IfConfAuthKeyId = _CabhPsDevCsaRip2IfConfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 1, 1, 1, 1, 1),
    _CabhPsDevCsaRip2IfConfAuthKeyId_Type()
)
cabhPsDevCsaRip2IfConfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhPsDevCsaRip2IfConfAuthKeyId.setStatus("current")
_CabhCdpCsaObjects_ObjectIdentity = ObjectIdentity
cabhCdpCsaObjects = _CabhCdpCsaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 4)
)


class _CabhCdpCsaServerEnable_Type(TruthValue):
    """Custom type cabhCdpCsaServerEnable based on TruthValue"""
    defaultValue = 1


_CabhCdpCsaServerEnable_Type.__name__ = "TruthValue"
_CabhCdpCsaServerEnable_Object = MibScalar
cabhCdpCsaServerEnable = _CabhCdpCsaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 1, 4, 1),
    _CabhCdpCsaServerEnable_Type()
)
cabhCdpCsaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpCsaServerEnable.setStatus("current")
_CabhPsCsaConformance_ObjectIdentity = ObjectIdentity
cabhPsCsaConformance = _CabhPsCsaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 2)
)
_CabhPsCsaCompliances_ObjectIdentity = ObjectIdentity
cabhPsCsaCompliances = _CabhPsCsaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 2, 1)
)
_CabhPsCsaGroups_ObjectIdentity = ObjectIdentity
cabhPsCsaGroups = _CabhPsCsaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 2, 2)
)
rip2IfStatEntry.registerAugmentions(
    ("CABH-PS-CSA-MIB",
     "cabhPsDevCsaRip2IfConfExtEntry")
)
cabhPsDevCsaRip2IfConfExtEntry.setIndexNames(*rip2IfStatEntry.getIndexNames())

# Managed Objects groups

cabhPsCsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 2, 2, 1)
)
cabhPsCsaGroup.setObjects(
      *(("CABH-PS-CSA-MIB", "cabhPsDevCsaRip2IfConfAuthKeyId"),
        ("CABH-PS-CSA-MIB", "cabhCdpCsaServerEnable"))
)
if mibBuilder.loadTexts:
    cabhPsCsaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhPsCsaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 7, 2, 1, 1)
)
cabhPsCsaCompliance.setObjects(
    ("CABH-PS-CSA-MIB", "cabhPsCsaGroup")
)
if mibBuilder.loadTexts:
    cabhPsCsaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-PS-CSA-MIB",
    **{"cabhPsCsaMib": cabhPsCsaMib,
       "cabhPsCsaNotifications": cabhPsCsaNotifications,
       "cabhPsCsaMibObjects": cabhPsCsaMibObjects,
       "cabhPsDevCsaObjects": cabhPsDevCsaObjects,
       "cabhPsDevCsaRipExtension": cabhPsDevCsaRipExtension,
       "cabhPsDevCsaRip2IfConfExtTable": cabhPsDevCsaRip2IfConfExtTable,
       "cabhPsDevCsaRip2IfConfExtEntry": cabhPsDevCsaRip2IfConfExtEntry,
       "cabhPsDevCsaRip2IfConfAuthKeyId": cabhPsDevCsaRip2IfConfAuthKeyId,
       "cabhCdpCsaObjects": cabhCdpCsaObjects,
       "cabhCdpCsaServerEnable": cabhCdpCsaServerEnable,
       "cabhPsCsaConformance": cabhPsCsaConformance,
       "cabhPsCsaCompliances": cabhPsCsaCompliances,
       "cabhPsCsaCompliance": cabhPsCsaCompliance,
       "cabhPsCsaGroups": cabhPsCsaGroups,
       "cabhPsCsaGroup": cabhPsCsaGroup}
)
