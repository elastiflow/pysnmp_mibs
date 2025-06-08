# SNMP MIB module (ZYXEL-LEGACY-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-LEGACY-PRIVATE-VLAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:16 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelLegacyPrivateVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLegacyPrivateVlanSetup_ObjectIdentity = ObjectIdentity
zyxelLegacyPrivateVlanSetup = _ZyxelLegacyPrivateVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1)
)
_ZyLegacyPrivateVlanMaxNumberOfVlans_Type = Integer32
_ZyLegacyPrivateVlanMaxNumberOfVlans_Object = MibScalar
zyLegacyPrivateVlanMaxNumberOfVlans = _ZyLegacyPrivateVlanMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 1),
    _ZyLegacyPrivateVlanMaxNumberOfVlans_Type()
)
zyLegacyPrivateVlanMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyLegacyPrivateVlanMaxNumberOfVlans.setStatus("current")
_ZyxelLegacyPrivateVlanTable_Object = MibTable
zyxelLegacyPrivateVlanTable = _ZyxelLegacyPrivateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelLegacyPrivateVlanTable.setStatus("current")
_ZyxelLegacyPrivateVlanEntry_Object = MibTableRow
zyxelLegacyPrivateVlanEntry = _ZyxelLegacyPrivateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1)
)
zyxelLegacyPrivateVlanEntry.setIndexNames(
    (0, "ZYXEL-LEGACY-PRIVATE-VLAN-MIB", "zyLegacyPrivateVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelLegacyPrivateVlanEntry.setStatus("current")


class _ZyLegacyPrivateVlanVid_Type(Integer32):
    """Custom type zyLegacyPrivateVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyLegacyPrivateVlanVid_Type.__name__ = "Integer32"
_ZyLegacyPrivateVlanVid_Object = MibTableColumn
zyLegacyPrivateVlanVid = _ZyLegacyPrivateVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 1),
    _ZyLegacyPrivateVlanVid_Type()
)
zyLegacyPrivateVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyLegacyPrivateVlanVid.setStatus("current")
_ZyLegacyPrivateVlanName_Type = DisplayString
_ZyLegacyPrivateVlanName_Object = MibTableColumn
zyLegacyPrivateVlanName = _ZyLegacyPrivateVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 2),
    _ZyLegacyPrivateVlanName_Type()
)
zyLegacyPrivateVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLegacyPrivateVlanName.setStatus("current")
_ZyLegacyPrivateVlanPromiscuousPorts_Type = PortList
_ZyLegacyPrivateVlanPromiscuousPorts_Object = MibTableColumn
zyLegacyPrivateVlanPromiscuousPorts = _ZyLegacyPrivateVlanPromiscuousPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 3),
    _ZyLegacyPrivateVlanPromiscuousPorts_Type()
)
zyLegacyPrivateVlanPromiscuousPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLegacyPrivateVlanPromiscuousPorts.setStatus("current")
_ZyLegacyPrivateVlanRowStatus_Type = RowStatus
_ZyLegacyPrivateVlanRowStatus_Object = MibTableColumn
zyLegacyPrivateVlanRowStatus = _ZyLegacyPrivateVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 4),
    _ZyLegacyPrivateVlanRowStatus_Type()
)
zyLegacyPrivateVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyLegacyPrivateVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LEGACY-PRIVATE-VLAN-MIB",
    **{"zyxelLegacyPrivateVlan": zyxelLegacyPrivateVlan,
       "zyxelLegacyPrivateVlanSetup": zyxelLegacyPrivateVlanSetup,
       "zyLegacyPrivateVlanMaxNumberOfVlans": zyLegacyPrivateVlanMaxNumberOfVlans,
       "zyxelLegacyPrivateVlanTable": zyxelLegacyPrivateVlanTable,
       "zyxelLegacyPrivateVlanEntry": zyxelLegacyPrivateVlanEntry,
       "zyLegacyPrivateVlanVid": zyLegacyPrivateVlanVid,
       "zyLegacyPrivateVlanName": zyLegacyPrivateVlanName,
       "zyLegacyPrivateVlanPromiscuousPorts": zyLegacyPrivateVlanPromiscuousPorts,
       "zyLegacyPrivateVlanRowStatus": zyLegacyPrivateVlanRowStatus}
)
