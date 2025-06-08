# SNMP MIB module (ZHONE-IUA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHONE-IUA-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:11:11 2025
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

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

(zhoneIua,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIua")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneIuaModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1)
)
if mibBuilder.loadTexts:
    zhoneIuaModule.setRevisions(
        ("2009-05-25 23:16",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneIuaServerCfg_ObjectIdentity = ObjectIdentity
zhoneIuaServerCfg = _ZhoneIuaServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1)
)
_ZhoneIuaServerTable_Object = MibTable
zhoneIuaServerTable = _ZhoneIuaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneIuaServerTable.setStatus("current")
_ZhoneIuaServerEntry_Object = MibTableRow
zhoneIuaServerEntry = _ZhoneIuaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1)
)
zhoneIuaServerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "ZHONE-IUA-MIB", "zhoneIuaServerAddressIndex"),
)
if mibBuilder.loadTexts:
    zhoneIuaServerEntry.setStatus("current")
_ZhoneIuaServerAddressIndex_Type = Unsigned32
_ZhoneIuaServerAddressIndex_Object = MibTableColumn
zhoneIuaServerAddressIndex = _ZhoneIuaServerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 1),
    _ZhoneIuaServerAddressIndex_Type()
)
zhoneIuaServerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIuaServerAddressIndex.setStatus("current")
_ZhoneIuaServerRowStatus_Type = ZhoneRowStatus
_ZhoneIuaServerRowStatus_Object = MibTableColumn
zhoneIuaServerRowStatus = _ZhoneIuaServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 2),
    _ZhoneIuaServerRowStatus_Type()
)
zhoneIuaServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIuaServerRowStatus.setStatus("current")
_ZhoneIuaServerAddress_Type = InetAddress
_ZhoneIuaServerAddress_Object = MibTableColumn
zhoneIuaServerAddress = _ZhoneIuaServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 3),
    _ZhoneIuaServerAddress_Type()
)
zhoneIuaServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIuaServerAddress.setStatus("current")


class _ZhoneIuaServerPortNumber_Type(Integer32):
    """Custom type zhoneIuaServerPortNumber based on Integer32"""
    defaultValue = 9900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneIuaServerPortNumber_Type.__name__ = "Integer32"
_ZhoneIuaServerPortNumber_Object = MibTableColumn
zhoneIuaServerPortNumber = _ZhoneIuaServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 4),
    _ZhoneIuaServerPortNumber_Type()
)
zhoneIuaServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIuaServerPortNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-IUA-MIB",
    **{"zhoneIuaModule": zhoneIuaModule,
       "zhoneIuaServerCfg": zhoneIuaServerCfg,
       "zhoneIuaServerTable": zhoneIuaServerTable,
       "zhoneIuaServerEntry": zhoneIuaServerEntry,
       "zhoneIuaServerAddressIndex": zhoneIuaServerAddressIndex,
       "zhoneIuaServerRowStatus": zhoneIuaServerRowStatus,
       "zhoneIuaServerAddress": zhoneIuaServerAddress,
       "zhoneIuaServerPortNumber": zhoneIuaServerPortNumber}
)
