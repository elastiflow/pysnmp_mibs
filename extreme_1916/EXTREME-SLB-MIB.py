# SNMP MIB module (EXTREME-SLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-SLB-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:33 2025
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

extremeSlb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeSlbRealServerTable_Object = MibTable
extremeSlbRealServerTable = _ExtremeSlbRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 1)
)
if mibBuilder.loadTexts:
    extremeSlbRealServerTable.setStatus("current")
_ExtremeSlbRealServerEntry_Object = MibTableRow
extremeSlbRealServerEntry = _ExtremeSlbRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 1, 1)
)
extremeSlbRealServerEntry.setIndexNames(
    (0, "EXTREME-SLB-MIB", "extremeSlbRealServerIpAddress"),
)
if mibBuilder.loadTexts:
    extremeSlbRealServerEntry.setStatus("current")
_ExtremeSlbRealServerIpAddress_Type = IpAddress
_ExtremeSlbRealServerIpAddress_Object = MibTableColumn
extremeSlbRealServerIpAddress = _ExtremeSlbRealServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 1, 1, 1),
    _ExtremeSlbRealServerIpAddress_Type()
)
extremeSlbRealServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSlbRealServerIpAddress.setStatus("current")
_ExtremeSlbRealServerUp_Type = TruthValue
_ExtremeSlbRealServerUp_Object = MibTableColumn
extremeSlbRealServerUp = _ExtremeSlbRealServerUp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 1, 1, 2),
    _ExtremeSlbRealServerUp_Type()
)
extremeSlbRealServerUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSlbRealServerUp.setStatus("current")
_ExtremeSlbRealAppTable_Object = MibTable
extremeSlbRealAppTable = _ExtremeSlbRealAppTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 2)
)
if mibBuilder.loadTexts:
    extremeSlbRealAppTable.setStatus("current")
_ExtremeSlbRealAppEntry_Object = MibTableRow
extremeSlbRealAppEntry = _ExtremeSlbRealAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 2, 1)
)
extremeSlbRealAppEntry.setIndexNames(
    (0, "EXTREME-SLB-MIB", "extremeSlbRealAppIpAddress"),
    (0, "EXTREME-SLB-MIB", "extremeSlbRealAppPort"),
)
if mibBuilder.loadTexts:
    extremeSlbRealAppEntry.setStatus("current")
_ExtremeSlbRealAppIpAddress_Type = IpAddress
_ExtremeSlbRealAppIpAddress_Object = MibTableColumn
extremeSlbRealAppIpAddress = _ExtremeSlbRealAppIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 2, 1, 1),
    _ExtremeSlbRealAppIpAddress_Type()
)
extremeSlbRealAppIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSlbRealAppIpAddress.setStatus("current")


class _ExtremeSlbRealAppPort_Type(Integer32):
    """Custom type extremeSlbRealAppPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeSlbRealAppPort_Type.__name__ = "Integer32"
_ExtremeSlbRealAppPort_Object = MibTableColumn
extremeSlbRealAppPort = _ExtremeSlbRealAppPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 2, 1, 2),
    _ExtremeSlbRealAppPort_Type()
)
extremeSlbRealAppPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSlbRealAppPort.setStatus("current")
_ExtremeSlbRealAppUp_Type = TruthValue
_ExtremeSlbRealAppUp_Object = MibTableColumn
extremeSlbRealAppUp = _ExtremeSlbRealAppUp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14, 2, 1, 3),
    _ExtremeSlbRealAppUp_Type()
)
extremeSlbRealAppUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSlbRealAppUp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-SLB-MIB",
    **{"extremeSlb": extremeSlb,
       "extremeSlbRealServerTable": extremeSlbRealServerTable,
       "extremeSlbRealServerEntry": extremeSlbRealServerEntry,
       "extremeSlbRealServerIpAddress": extremeSlbRealServerIpAddress,
       "extremeSlbRealServerUp": extremeSlbRealServerUp,
       "extremeSlbRealAppTable": extremeSlbRealAppTable,
       "extremeSlbRealAppEntry": extremeSlbRealAppEntry,
       "extremeSlbRealAppIpAddress": extremeSlbRealAppIpAddress,
       "extremeSlbRealAppPort": extremeSlbRealAppPort,
       "extremeSlbRealAppUp": extremeSlbRealAppUp}
)
