# SNMP MIB module (CISCOSB-MULTISESSIONTERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-MULTISESSIONTERMINAL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:46 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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


# MODULE-IDENTITY

rlMultiSessionTerminal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 69)
)
if mibBuilder.loadTexts:
    rlMultiSessionTerminal.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlTerminalDebugModePassword_Type(DisplayString):
    """Custom type rlTerminalDebugModePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlTerminalDebugModePassword_Type.__name__ = "DisplayString"
_RlTerminalDebugModePassword_Object = MibScalar
rlTerminalDebugModePassword = _RlTerminalDebugModePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 69, 1),
    _RlTerminalDebugModePassword_Type()
)
rlTerminalDebugModePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTerminalDebugModePassword.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-MULTISESSIONTERMINAL-MIB",
    **{"rlMultiSessionTerminal": rlMultiSessionTerminal,
       "rlTerminalDebugModePassword": rlTerminalDebugModePassword}
)
