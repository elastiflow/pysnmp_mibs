# SNMP MIB module (EXTREME-VC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-VC-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:41:50 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeVC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeVCLinkTable_Object = MibTable
extremeVCLinkTable = _ExtremeVCLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1)
)
if mibBuilder.loadTexts:
    extremeVCLinkTable.setStatus("deprecated")
_ExtremeVCLinkEntry_Object = MibTableRow
extremeVCLinkEntry = _ExtremeVCLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1)
)
extremeVCLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeVCLinkEntry.setStatus("deprecated")
_ExtremeVCLinkValid_Type = TruthValue
_ExtremeVCLinkValid_Object = MibTableColumn
extremeVCLinkValid = _ExtremeVCLinkValid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 1),
    _ExtremeVCLinkValid_Type()
)
extremeVCLinkValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkValid.setStatus("deprecated")
_ExtremeVCLinkDeviceId_Type = Integer32
_ExtremeVCLinkDeviceId_Object = MibTableColumn
extremeVCLinkDeviceId = _ExtremeVCLinkDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 2),
    _ExtremeVCLinkDeviceId_Type()
)
extremeVCLinkDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkDeviceId.setStatus("deprecated")
_ExtremeVCLinkPortIndex_Type = Integer32
_ExtremeVCLinkPortIndex_Object = MibTableColumn
extremeVCLinkPortIndex = _ExtremeVCLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 3),
    _ExtremeVCLinkPortIndex_Type()
)
extremeVCLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVCLinkPortIndex.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-VC-MIB",
    **{"extremeVC": extremeVC,
       "extremeVCLinkTable": extremeVCLinkTable,
       "extremeVCLinkEntry": extremeVCLinkEntry,
       "extremeVCLinkValid": extremeVCLinkValid,
       "extremeVCLinkDeviceId": extremeVCLinkDeviceId,
       "extremeVCLinkPortIndex": extremeVCLinkPortIndex}
)
