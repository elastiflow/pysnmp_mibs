# SNMP MIB module (ZYXEL-MAC-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-MAC-AUTHENTICATION-MIB.mib
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

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


# MODULE-IDENTITY

zyxelMacAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacAuthenticationSetup_ObjectIdentity = ObjectIdentity
zyxelMacAuthenticationSetup = _ZyxelMacAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1)
)
_ZyMacAuthenticationState_Type = EnabledStatus
_ZyMacAuthenticationState_Object = MibScalar
zyMacAuthenticationState = _ZyMacAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 1),
    _ZyMacAuthenticationState_Type()
)
zyMacAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationState.setStatus("current")
_ZyMacAuthenticationNamePrefix_Type = DisplayString
_ZyMacAuthenticationNamePrefix_Object = MibScalar
zyMacAuthenticationNamePrefix = _ZyMacAuthenticationNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 2),
    _ZyMacAuthenticationNamePrefix_Type()
)
zyMacAuthenticationNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationNamePrefix.setStatus("current")
_ZyMacAuthenticationPassword_Type = DisplayString
_ZyMacAuthenticationPassword_Object = MibScalar
zyMacAuthenticationPassword = _ZyMacAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 3),
    _ZyMacAuthenticationPassword_Type()
)
zyMacAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPassword.setStatus("current")
_ZyMacAuthenticationTimeout_Type = Integer32
_ZyMacAuthenticationTimeout_Object = MibScalar
zyMacAuthenticationTimeout = _ZyMacAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 4),
    _ZyMacAuthenticationTimeout_Type()
)
zyMacAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationTimeout.setStatus("current")
_ZyxelMacAuthenticationPortTable_Object = MibTable
zyxelMacAuthenticationPortTable = _ZyxelMacAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelMacAuthenticationPortTable.setStatus("current")
_ZyxelMacAuthenticationPortEntry_Object = MibTableRow
zyxelMacAuthenticationPortEntry = _ZyxelMacAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1)
)
zyxelMacAuthenticationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMacAuthenticationPortEntry.setStatus("current")
_ZyMacAuthenticationPortState_Type = EnabledStatus
_ZyMacAuthenticationPortState_Object = MibTableColumn
zyMacAuthenticationPortState = _ZyMacAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1, 1),
    _ZyMacAuthenticationPortState_Type()
)
zyMacAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPortState.setStatus("current")


class _ZyMacAuthenticationPortTrustedVlan1k_Type(OctetString):
    """Custom type zyMacAuthenticationPortTrustedVlan1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMacAuthenticationPortTrustedVlan1k_Type.__name__ = "OctetString"
_ZyMacAuthenticationPortTrustedVlan1k_Object = MibTableColumn
zyMacAuthenticationPortTrustedVlan1k = _ZyMacAuthenticationPortTrustedVlan1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1, 2),
    _ZyMacAuthenticationPortTrustedVlan1k_Type()
)
zyMacAuthenticationPortTrustedVlan1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPortTrustedVlan1k.setStatus("current")


class _ZyMacAuthenticationPortTrustedVlan2k_Type(OctetString):
    """Custom type zyMacAuthenticationPortTrustedVlan2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMacAuthenticationPortTrustedVlan2k_Type.__name__ = "OctetString"
_ZyMacAuthenticationPortTrustedVlan2k_Object = MibTableColumn
zyMacAuthenticationPortTrustedVlan2k = _ZyMacAuthenticationPortTrustedVlan2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1, 3),
    _ZyMacAuthenticationPortTrustedVlan2k_Type()
)
zyMacAuthenticationPortTrustedVlan2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPortTrustedVlan2k.setStatus("current")


class _ZyMacAuthenticationPortTrustedVlan3k_Type(OctetString):
    """Custom type zyMacAuthenticationPortTrustedVlan3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMacAuthenticationPortTrustedVlan3k_Type.__name__ = "OctetString"
_ZyMacAuthenticationPortTrustedVlan3k_Object = MibTableColumn
zyMacAuthenticationPortTrustedVlan3k = _ZyMacAuthenticationPortTrustedVlan3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1, 4),
    _ZyMacAuthenticationPortTrustedVlan3k_Type()
)
zyMacAuthenticationPortTrustedVlan3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPortTrustedVlan3k.setStatus("current")


class _ZyMacAuthenticationPortTrustedVlan4k_Type(OctetString):
    """Custom type zyMacAuthenticationPortTrustedVlan4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMacAuthenticationPortTrustedVlan4k_Type.__name__ = "OctetString"
_ZyMacAuthenticationPortTrustedVlan4k_Object = MibTableColumn
zyMacAuthenticationPortTrustedVlan4k = _ZyMacAuthenticationPortTrustedVlan4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1, 5),
    _ZyMacAuthenticationPortTrustedVlan4k_Type()
)
zyMacAuthenticationPortTrustedVlan4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPortTrustedVlan4k.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MAC-AUTHENTICATION-MIB",
    **{"zyxelMacAuthentication": zyxelMacAuthentication,
       "zyxelMacAuthenticationSetup": zyxelMacAuthenticationSetup,
       "zyMacAuthenticationState": zyMacAuthenticationState,
       "zyMacAuthenticationNamePrefix": zyMacAuthenticationNamePrefix,
       "zyMacAuthenticationPassword": zyMacAuthenticationPassword,
       "zyMacAuthenticationTimeout": zyMacAuthenticationTimeout,
       "zyxelMacAuthenticationPortTable": zyxelMacAuthenticationPortTable,
       "zyxelMacAuthenticationPortEntry": zyxelMacAuthenticationPortEntry,
       "zyMacAuthenticationPortState": zyMacAuthenticationPortState,
       "zyMacAuthenticationPortTrustedVlan1k": zyMacAuthenticationPortTrustedVlan1k,
       "zyMacAuthenticationPortTrustedVlan2k": zyMacAuthenticationPortTrustedVlan2k,
       "zyMacAuthenticationPortTrustedVlan3k": zyMacAuthenticationPortTrustedVlan3k,
       "zyMacAuthenticationPortTrustedVlan4k": zyMacAuthenticationPortTrustedVlan4k}
)
