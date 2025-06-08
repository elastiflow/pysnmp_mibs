# SNMP MIB module (LARCH-NETWORKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/beeper_47108/LARCH-NETWORKS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:42:51 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

larchNetworks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47108)
)
if mibBuilder.loadTexts:
    larchNetworks.setRevisions(
        ("1999-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cellular_ObjectIdentity = ObjectIdentity
cellular = _Cellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47108, 1)
)
_CellularTables_ObjectIdentity = ObjectIdentity
cellularTables = _CellularTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1)
)
_CellularInterfaceTable_Object = MibTable
cellularInterfaceTable = _CellularInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cellularInterfaceTable.setStatus("current")
_CellularInterfaceEntry_Object = MibTableRow
cellularInterfaceEntry = _CellularInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1)
)
cellularInterfaceEntry.setIndexNames(
    (0, "LARCH-NETWORKS-MIB", "cellularInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cellularInterfaceEntry.setStatus("current")


class _CellularInterfaceIndex_Type(Integer32):
    """Custom type cellularInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CellularInterfaceIndex_Type.__name__ = "Integer32"
_CellularInterfaceIndex_Object = MibTableColumn
cellularInterfaceIndex = _CellularInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 1),
    _CellularInterfaceIndex_Type()
)
cellularInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceIndex.setStatus("current")
_CellularInterfaceServiceProvider_Type = SnmpAdminString
_CellularInterfaceServiceProvider_Object = MibTableColumn
cellularInterfaceServiceProvider = _CellularInterfaceServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 2),
    _CellularInterfaceServiceProvider_Type()
)
cellularInterfaceServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceServiceProvider.setStatus("current")


class _CellularInterfaceBand_Type(Integer32):
    """Custom type cellularInterfaceBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("invalid", 2),
          ("none", 3),
          ("gsm850", 4),
          ("gsm900", 5),
          ("gsm1800", 6),
          ("gsm1900", 7),
          ("wcdma800", 8),
          ("wcdma850", 9),
          ("wcdma1900", 10),
          ("wcdma2100", 11),
          ("lteBand", 12))
    )


_CellularInterfaceBand_Type.__name__ = "Integer32"
_CellularInterfaceBand_Object = MibTableColumn
cellularInterfaceBand = _CellularInterfaceBand_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 3),
    _CellularInterfaceBand_Type()
)
cellularInterfaceBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceBand.setStatus("current")
_CellularInterfaceProtocol_Type = SnmpAdminString
_CellularInterfaceProtocol_Object = MibTableColumn
cellularInterfaceProtocol = _CellularInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 4),
    _CellularInterfaceProtocol_Type()
)
cellularInterfaceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularInterfaceProtocol.setStatus("current")
_CellularInterfaceUplinkPeakRate_Type = Integer32
_CellularInterfaceUplinkPeakRate_Object = MibTableColumn
cellularInterfaceUplinkPeakRate = _CellularInterfaceUplinkPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 5),
    _CellularInterfaceUplinkPeakRate_Type()
)
cellularInterfaceUplinkPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceUplinkPeakRate.setStatus("current")
_CellularInterfaceDownlinkPeakRate_Type = Integer32
_CellularInterfaceDownlinkPeakRate_Object = MibTableColumn
cellularInterfaceDownlinkPeakRate = _CellularInterfaceDownlinkPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 6),
    _CellularInterfaceDownlinkPeakRate_Type()
)
cellularInterfaceDownlinkPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceDownlinkPeakRate.setStatus("current")
_CellularInterfaceActualUplinkRate_Type = Integer32
_CellularInterfaceActualUplinkRate_Object = MibTableColumn
cellularInterfaceActualUplinkRate = _CellularInterfaceActualUplinkRate_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 7),
    _CellularInterfaceActualUplinkRate_Type()
)
cellularInterfaceActualUplinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceActualUplinkRate.setStatus("current")
_CellularInterfaceActualDownlinkRate_Type = Integer32
_CellularInterfaceActualDownlinkRate_Object = MibTableColumn
cellularInterfaceActualDownlinkRate = _CellularInterfaceActualDownlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 8),
    _CellularInterfaceActualDownlinkRate_Type()
)
cellularInterfaceActualDownlinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceActualDownlinkRate.setStatus("current")
_CellularInterfaceSignalStrength_Type = SnmpAdminString
_CellularInterfaceSignalStrength_Object = MibTableColumn
cellularInterfaceSignalStrength = _CellularInterfaceSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 9),
    _CellularInterfaceSignalStrength_Type()
)
cellularInterfaceSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceSignalStrength.setStatus("current")
_CellularInterfaceSNR_Type = Integer32
_CellularInterfaceSNR_Object = MibTableColumn
cellularInterfaceSNR = _CellularInterfaceSNR_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 1, 1, 10),
    _CellularInterfaceSNR_Type()
)
cellularInterfaceSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularInterfaceSNR.setStatus("current")
_CellularSystemInfo_ObjectIdentity = ObjectIdentity
cellularSystemInfo = _CellularSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 2)
)
_CellularSystemUsername_Type = SnmpAdminString
_CellularSystemUsername_Object = MibScalar
cellularSystemUsername = _CellularSystemUsername_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 2, 1),
    _CellularSystemUsername_Type()
)
cellularSystemUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularSystemUsername.setStatus("current")
_CellularSystemPassword_Type = SnmpAdminString
_CellularSystemPassword_Object = MibScalar
cellularSystemPassword = _CellularSystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 2, 2),
    _CellularSystemPassword_Type()
)
cellularSystemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularSystemPassword.setStatus("current")
_CellularSystemServerIP_Type = IpAddress
_CellularSystemServerIP_Object = MibScalar
cellularSystemServerIP = _CellularSystemServerIP_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 2, 3),
    _CellularSystemServerIP_Type()
)
cellularSystemServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularSystemServerIP.setStatus("current")
_CellularSystemToken_Type = Integer32
_CellularSystemToken_Object = MibScalar
cellularSystemToken = _CellularSystemToken_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 2, 4),
    _CellularSystemToken_Type()
)
cellularSystemToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularSystemToken.setStatus("current")
_CellularSystemTrafficSharingMethods_Type = SnmpAdminString
_CellularSystemTrafficSharingMethods_Object = MibScalar
cellularSystemTrafficSharingMethods = _CellularSystemTrafficSharingMethods_Object(
    (1, 3, 6, 1, 4, 1, 47108, 1, 1, 2, 5),
    _CellularSystemTrafficSharingMethods_Type()
)
cellularSystemTrafficSharingMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularSystemTrafficSharingMethods.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LARCH-NETWORKS-MIB",
    **{"larchNetworks": larchNetworks,
       "cellular": cellular,
       "cellularTables": cellularTables,
       "cellularInterfaceTable": cellularInterfaceTable,
       "cellularInterfaceEntry": cellularInterfaceEntry,
       "cellularInterfaceIndex": cellularInterfaceIndex,
       "cellularInterfaceServiceProvider": cellularInterfaceServiceProvider,
       "cellularInterfaceBand": cellularInterfaceBand,
       "cellularInterfaceProtocol": cellularInterfaceProtocol,
       "cellularInterfaceUplinkPeakRate": cellularInterfaceUplinkPeakRate,
       "cellularInterfaceDownlinkPeakRate": cellularInterfaceDownlinkPeakRate,
       "cellularInterfaceActualUplinkRate": cellularInterfaceActualUplinkRate,
       "cellularInterfaceActualDownlinkRate": cellularInterfaceActualDownlinkRate,
       "cellularInterfaceSignalStrength": cellularInterfaceSignalStrength,
       "cellularInterfaceSNR": cellularInterfaceSNR,
       "cellularSystemInfo": cellularSystemInfo,
       "cellularSystemUsername": cellularSystemUsername,
       "cellularSystemPassword": cellularSystemPassword,
       "cellularSystemServerIP": cellularSystemServerIP,
       "cellularSystemToken": cellularSystemToken,
       "cellularSystemTrafficSharingMethods": cellularSystemTrafficSharingMethods}
)
