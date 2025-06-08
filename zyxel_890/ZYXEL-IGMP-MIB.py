# SNMP MIB module (ZYXEL-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IGMP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:21 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")

(zyRouteDomainIpAddress,
 zyRouteDomainIpMaskBits) = mibBuilder.importSymbols(
    "ZYXEL-IP-FORWARD-MIB",
    "zyRouteDomainIpAddress",
    "zyRouteDomainIpMaskBits")


# MODULE-IDENTITY

zyxelIgmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIgmpSetup_ObjectIdentity = ObjectIdentity
zyxelIgmpSetup = _ZyxelIgmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1)
)
_ZyIgmpState_Type = EnabledStatus
_ZyIgmpState_Object = MibScalar
zyIgmpState = _ZyIgmpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 1),
    _ZyIgmpState_Type()
)
zyIgmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpState.setStatus("current")
_ZyxelIgmpRouteDomainTable_Object = MibTable
zyxelIgmpRouteDomainTable = _ZyxelIgmpRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelIgmpRouteDomainTable.setStatus("current")
_ZyxelIgmpRouteDomainEntry_Object = MibTableRow
zyxelIgmpRouteDomainEntry = _ZyxelIgmpRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2, 1)
)
zyxelIgmpRouteDomainEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelIgmpRouteDomainEntry.setStatus("current")


class _ZyIgmpRouteDomainVersion_Type(Integer32):
    """Custom type zyIgmpRouteDomainVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("igmpV1", 1),
          ("igmpV2", 2),
          ("igmpV3", 3))
    )


_ZyIgmpRouteDomainVersion_Type.__name__ = "Integer32"
_ZyIgmpRouteDomainVersion_Object = MibTableColumn
zyIgmpRouteDomainVersion = _ZyIgmpRouteDomainVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2, 1, 1),
    _ZyIgmpRouteDomainVersion_Type()
)
zyIgmpRouteDomainVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpRouteDomainVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IGMP-MIB",
    **{"zyxelIgmp": zyxelIgmp,
       "zyxelIgmpSetup": zyxelIgmpSetup,
       "zyIgmpState": zyIgmpState,
       "zyxelIgmpRouteDomainTable": zyxelIgmpRouteDomainTable,
       "zyxelIgmpRouteDomainEntry": zyxelIgmpRouteDomainEntry,
       "zyIgmpRouteDomainVersion": zyIgmpRouteDomainVersion}
)
