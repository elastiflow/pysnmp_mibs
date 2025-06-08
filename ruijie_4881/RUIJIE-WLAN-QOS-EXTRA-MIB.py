# SNMP MIB module (RUIJIE-WLAN-QOS-EXTRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-QOS-EXTRA-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:52:30 2025
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

(ruijieApCfgRadioId,
 ruijieApMacAddr,
 ruijieApgWlanId,
 ruijieStaMacAddr) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApCfgRadioId",
    "ruijieApMacAddr",
    "ruijieApgWlanId",
    "ruijieStaMacAddr")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieWlanQosExtraMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60)
)
if mibBuilder.loadTexts:
    ruijieWlanQosExtraMib.setRevisions(
        ("2009-09-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWlanDeviceWMMObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDeviceWMMObjects = _RuijieWlanDeviceWMMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 1)
)
_RuijieWMMStatusTable_Object = MibTable
ruijieWMMStatusTable = _RuijieWMMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWMMStatusTable.setStatus("current")
_RuijieWMMStatusEntry_Object = MibTableRow
ruijieWMMStatusEntry = _RuijieWMMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 1, 1, 1)
)
ruijieWMMStatusEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWMMStatusEntry.setStatus("current")


class _RuijieWMMStatus_Type(TruthValue):
    """Custom type ruijieWMMStatus based on TruthValue"""
    defaultValue = 1


_RuijieWMMStatus_Type.__name__ = "TruthValue"
_RuijieWMMStatus_Object = MibTableColumn
ruijieWMMStatus = _RuijieWMMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 1, 1, 1, 1),
    _RuijieWMMStatus_Type()
)
ruijieWMMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWMMStatus.setStatus("current")


class _RuijieAPSDStatus_Type(TruthValue):
    """Custom type ruijieAPSDStatus based on TruthValue"""
    defaultValue = 1


_RuijieAPSDStatus_Type.__name__ = "TruthValue"
_RuijieAPSDStatus_Object = MibTableColumn
ruijieAPSDStatus = _RuijieAPSDStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 1, 1, 1, 2),
    _RuijieAPSDStatus_Type()
)
ruijieAPSDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPSDStatus.setStatus("current")


class _RuijieSMPSStatus_Type(TruthValue):
    """Custom type ruijieSMPSStatus based on TruthValue"""
    defaultValue = 1


_RuijieSMPSStatus_Type.__name__ = "TruthValue"
_RuijieSMPSStatus_Object = MibTableColumn
ruijieSMPSStatus = _RuijieSMPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 1, 1, 1, 3),
    _RuijieSMPSStatus_Type()
)
ruijieSMPSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSMPSStatus.setStatus("current")
_RuijieWlanDeviceEDCAObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDeviceEDCAObjects = _RuijieWlanDeviceEDCAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2)
)
_Ruijiedot11EDCATable_Object = MibTable
ruijiedot11EDCATable = _Ruijiedot11EDCATable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1)
)
if mibBuilder.loadTexts:
    ruijiedot11EDCATable.setStatus("current")
_Ruijiedot11EDCAEntry_Object = MibTableRow
ruijiedot11EDCAEntry = _Ruijiedot11EDCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1)
)
ruijiedot11EDCAEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableIndex"),
)
if mibBuilder.loadTexts:
    ruijiedot11EDCAEntry.setStatus("current")


class _Ruijiedot11EDCATableIndex_Type(Integer32):
    """Custom type ruijiedot11EDCATableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ruijiedot11EDCATableIndex_Type.__name__ = "Integer32"
_Ruijiedot11EDCATableIndex_Object = MibTableColumn
ruijiedot11EDCATableIndex = _Ruijiedot11EDCATableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 1),
    _Ruijiedot11EDCATableIndex_Type()
)
ruijiedot11EDCATableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableIndex.setStatus("current")


class _Ruijiedot11EDCATableCWmin_Type(Integer32):
    """Custom type ruijiedot11EDCATableCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ruijiedot11EDCATableCWmin_Type.__name__ = "Integer32"
_Ruijiedot11EDCATableCWmin_Object = MibTableColumn
ruijiedot11EDCATableCWmin = _Ruijiedot11EDCATableCWmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 2),
    _Ruijiedot11EDCATableCWmin_Type()
)
ruijiedot11EDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableCWmin.setStatus("current")


class _Ruijiedot11EDCATableCWmax_Type(Integer32):
    """Custom type ruijiedot11EDCATableCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ruijiedot11EDCATableCWmax_Type.__name__ = "Integer32"
_Ruijiedot11EDCATableCWmax_Object = MibTableColumn
ruijiedot11EDCATableCWmax = _Ruijiedot11EDCATableCWmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 3),
    _Ruijiedot11EDCATableCWmax_Type()
)
ruijiedot11EDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableCWmax.setStatus("current")


class _Ruijiedot11EDCATableAIFSN_Type(Integer32):
    """Custom type ruijiedot11EDCATableAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Ruijiedot11EDCATableAIFSN_Type.__name__ = "Integer32"
_Ruijiedot11EDCATableAIFSN_Object = MibTableColumn
ruijiedot11EDCATableAIFSN = _Ruijiedot11EDCATableAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 4),
    _Ruijiedot11EDCATableAIFSN_Type()
)
ruijiedot11EDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableAIFSN.setStatus("current")


class _Ruijiedot11EDCATableTXOPLimit_Type(Integer32):
    """Custom type ruijiedot11EDCATableTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ruijiedot11EDCATableTXOPLimit_Type.__name__ = "Integer32"
_Ruijiedot11EDCATableTXOPLimit_Object = MibTableColumn
ruijiedot11EDCATableTXOPLimit = _Ruijiedot11EDCATableTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 5),
    _Ruijiedot11EDCATableTXOPLimit_Type()
)
ruijiedot11EDCATableTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableTXOPLimit.setStatus("current")


class _Ruijiedot11EDCATableMSDULifetime_Type(Integer32):
    """Custom type ruijiedot11EDCATableMSDULifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Ruijiedot11EDCATableMSDULifetime_Type.__name__ = "Integer32"
_Ruijiedot11EDCATableMSDULifetime_Object = MibTableColumn
ruijiedot11EDCATableMSDULifetime = _Ruijiedot11EDCATableMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 6),
    _Ruijiedot11EDCATableMSDULifetime_Type()
)
ruijiedot11EDCATableMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableMSDULifetime.setStatus("current")
_Ruijiedot11EDCATableMandatory_Type = TruthValue
_Ruijiedot11EDCATableMandatory_Object = MibTableColumn
ruijiedot11EDCATableMandatory = _Ruijiedot11EDCATableMandatory_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 1, 1, 7),
    _Ruijiedot11EDCATableMandatory_Type()
)
ruijiedot11EDCATableMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11EDCATableMandatory.setStatus("current")
_Ruijiedot11QAPEDCATable_Object = MibTable
ruijiedot11QAPEDCATable = _Ruijiedot11QAPEDCATable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2)
)
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATable.setStatus("current")
_Ruijiedot11QAPEDCAEntry_Object = MibTableRow
ruijiedot11QAPEDCAEntry = _Ruijiedot11QAPEDCAEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1)
)
ruijiedot11QAPEDCAEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCAEntry.setStatus("current")


class _Ruijiedot11QAPEDCATableIndex_Type(Integer32):
    """Custom type ruijiedot11QAPEDCATableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ruijiedot11QAPEDCATableIndex_Type.__name__ = "Integer32"
_Ruijiedot11QAPEDCATableIndex_Object = MibTableColumn
ruijiedot11QAPEDCATableIndex = _Ruijiedot11QAPEDCATableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 1),
    _Ruijiedot11QAPEDCATableIndex_Type()
)
ruijiedot11QAPEDCATableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableIndex.setStatus("current")


class _Ruijiedot11QAPEDCATableCWmin_Type(Integer32):
    """Custom type ruijiedot11QAPEDCATableCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ruijiedot11QAPEDCATableCWmin_Type.__name__ = "Integer32"
_Ruijiedot11QAPEDCATableCWmin_Object = MibTableColumn
ruijiedot11QAPEDCATableCWmin = _Ruijiedot11QAPEDCATableCWmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 2),
    _Ruijiedot11QAPEDCATableCWmin_Type()
)
ruijiedot11QAPEDCATableCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableCWmin.setStatus("current")


class _Ruijiedot11QAPEDCATableCWmax_Type(Integer32):
    """Custom type ruijiedot11QAPEDCATableCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ruijiedot11QAPEDCATableCWmax_Type.__name__ = "Integer32"
_Ruijiedot11QAPEDCATableCWmax_Object = MibTableColumn
ruijiedot11QAPEDCATableCWmax = _Ruijiedot11QAPEDCATableCWmax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 3),
    _Ruijiedot11QAPEDCATableCWmax_Type()
)
ruijiedot11QAPEDCATableCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableCWmax.setStatus("current")


class _Ruijiedot11QAPEDCATableAIFSN_Type(Integer32):
    """Custom type ruijiedot11QAPEDCATableAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ruijiedot11QAPEDCATableAIFSN_Type.__name__ = "Integer32"
_Ruijiedot11QAPEDCATableAIFSN_Object = MibTableColumn
ruijiedot11QAPEDCATableAIFSN = _Ruijiedot11QAPEDCATableAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 4),
    _Ruijiedot11QAPEDCATableAIFSN_Type()
)
ruijiedot11QAPEDCATableAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableAIFSN.setStatus("current")


class _Ruijiedot11QAPEDCATableTXOPLimit_Type(Integer32):
    """Custom type ruijiedot11QAPEDCATableTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ruijiedot11QAPEDCATableTXOPLimit_Type.__name__ = "Integer32"
_Ruijiedot11QAPEDCATableTXOPLimit_Object = MibTableColumn
ruijiedot11QAPEDCATableTXOPLimit = _Ruijiedot11QAPEDCATableTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 5),
    _Ruijiedot11QAPEDCATableTXOPLimit_Type()
)
ruijiedot11QAPEDCATableTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableTXOPLimit.setStatus("current")


class _Ruijiedot11QAPEDCATableMSDULifetime_Type(Integer32):
    """Custom type ruijiedot11QAPEDCATableMSDULifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Ruijiedot11QAPEDCATableMSDULifetime_Type.__name__ = "Integer32"
_Ruijiedot11QAPEDCATableMSDULifetime_Object = MibTableColumn
ruijiedot11QAPEDCATableMSDULifetime = _Ruijiedot11QAPEDCATableMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 6),
    _Ruijiedot11QAPEDCATableMSDULifetime_Type()
)
ruijiedot11QAPEDCATableMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableMSDULifetime.setStatus("current")
_Ruijiedot11QAPEDCATableMandatory_Type = TruthValue
_Ruijiedot11QAPEDCATableMandatory_Object = MibTableColumn
ruijiedot11QAPEDCATableMandatory = _Ruijiedot11QAPEDCATableMandatory_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 2, 1, 7),
    _Ruijiedot11QAPEDCATableMandatory_Type()
)
ruijiedot11QAPEDCATableMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot11QAPEDCATableMandatory.setStatus("current")
_RuijieWlanEDCATable_Object = MibTable
ruijieWlanEDCATable = _RuijieWlanEDCATable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieWlanEDCATable.setStatus("current")
_RuijieEDCAStatusEntry_Object = MibTableRow
ruijieEDCAStatusEntry = _RuijieEDCAStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 3, 1)
)
ruijieEDCAStatusEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    ruijieEDCAStatusEntry.setStatus("current")


class _RuijieQAPEDCAqueuedepth_Type(Integer32):
    """Custom type ruijieQAPEDCAqueuedepth based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RuijieQAPEDCAqueuedepth_Type.__name__ = "Integer32"
_RuijieQAPEDCAqueuedepth_Object = MibTableColumn
ruijieQAPEDCAqueuedepth = _RuijieQAPEDCAqueuedepth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 3, 1, 1),
    _RuijieQAPEDCAqueuedepth_Type()
)
ruijieQAPEDCAqueuedepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQAPEDCAqueuedepth.setStatus("current")


class _RuijieQAPEDCAcacPolicy_Type(Integer32):
    """Custom type ruijieQAPEDCAcacPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nocac", 0),
          ("usernum-based", 1),
          ("channelutilization-based", 2))
    )


_RuijieQAPEDCAcacPolicy_Type.__name__ = "Integer32"
_RuijieQAPEDCAcacPolicy_Object = MibTableColumn
ruijieQAPEDCAcacPolicy = _RuijieQAPEDCAcacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 3, 1, 2),
    _RuijieQAPEDCAcacPolicy_Type()
)
ruijieQAPEDCAcacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQAPEDCAcacPolicy.setStatus("current")


class _RuijieQAPEDCAcacParam_Type(Integer32):
    """Custom type ruijieQAPEDCAcacParam based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieQAPEDCAcacParam_Type.__name__ = "Integer32"
_RuijieQAPEDCAcacParam_Object = MibTableColumn
ruijieQAPEDCAcacParam = _RuijieQAPEDCAcacParam_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 2, 3, 1, 3),
    _RuijieQAPEDCAcacParam_Type()
)
ruijieQAPEDCAcacParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQAPEDCAcacParam.setStatus("current")
_RuijieWlanDevicePrivMappingObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDevicePrivMappingObjects = _RuijieWlanDevicePrivMappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3)
)
_RuijieWlanDevicePrivMappingWlanDefaultObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDevicePrivMappingWlanDefaultObjects = _RuijieWlanDevicePrivMappingWlanDefaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 1)
)
_RuijieWlanDefaultACTable_Object = MibTable
ruijieWlanDefaultACTable = _RuijieWlanDefaultACTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWlanDefaultACTable.setStatus("current")
_RuijieWlanDefaultACEntry_Object = MibTableRow
ruijieWlanDefaultACEntry = _RuijieWlanDefaultACEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 1, 1, 1)
)
ruijieWlanDefaultACEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWlanDefaultACEntry.setStatus("current")
_RuijieWlanDefualtACnum_Type = Integer32
_RuijieWlanDefualtACnum_Object = MibTableColumn
ruijieWlanDefualtACnum = _RuijieWlanDefualtACnum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 1, 1, 1, 1),
    _RuijieWlanDefualtACnum_Type()
)
ruijieWlanDefualtACnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanDefualtACnum.setStatus("current")
_RuijieWlanMaxstadot1ptag_Type = Integer32
_RuijieWlanMaxstadot1ptag_Object = MibTableColumn
ruijieWlanMaxstadot1ptag = _RuijieWlanMaxstadot1ptag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 1, 1, 1, 2),
    _RuijieWlanMaxstadot1ptag_Type()
)
ruijieWlanMaxstadot1ptag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanMaxstadot1ptag.setStatus("current")
_RuijieWlanDevicePrivMappingAPDefaultObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDevicePrivMappingAPDefaultObjects = _RuijieWlanDevicePrivMappingAPDefaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2)
)
_RuijiePrivMappingAPstatusTable_Object = MibTable
ruijiePrivMappingAPstatusTable = _RuijiePrivMappingAPstatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ruijiePrivMappingAPstatusTable.setStatus("current")
_RuijieAPdefaultStatusMappingEntry_Object = MibTableRow
ruijieAPdefaultStatusMappingEntry = _RuijieAPdefaultStatusMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 1, 1)
)
ruijieAPdefaultStatusMappingEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieAPdefaultStatusMappingEntry.setStatus("current")


class _Ruijiedot1pmappingstatus_Type(Integer32):
    """Custom type ruijiedot1pmappingstatus based on Integer32"""
    defaultValue = 0


_Ruijiedot1pmappingstatus_Type.__name__ = "Integer32"
_Ruijiedot1pmappingstatus_Object = MibTableColumn
ruijiedot1pmappingstatus = _Ruijiedot1pmappingstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 1, 1, 1),
    _Ruijiedot1pmappingstatus_Type()
)
ruijiedot1pmappingstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedot1pmappingstatus.setStatus("current")


class _Ruijiedscpmappingstatus_Type(Integer32):
    """Custom type ruijiedscpmappingstatus based on Integer32"""
    defaultValue = 0


_Ruijiedscpmappingstatus_Type.__name__ = "Integer32"
_Ruijiedscpmappingstatus_Object = MibTableColumn
ruijiedscpmappingstatus = _Ruijiedscpmappingstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 1, 1, 2),
    _Ruijiedscpmappingstatus_Type()
)
ruijiedscpmappingstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiedscpmappingstatus.setStatus("current")
_RuijiePrivMappingAPDefaultTable_Object = MibTable
ruijiePrivMappingAPDefaultTable = _RuijiePrivMappingAPDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ruijiePrivMappingAPDefaultTable.setStatus("current")
_RuijiePrivMappingAPDefaultEntry_Object = MibTableRow
ruijiePrivMappingAPDefaultEntry = _RuijiePrivMappingAPDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 2, 1)
)
ruijiePrivMappingAPDefaultEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableIndex"),
)
if mibBuilder.loadTexts:
    ruijiePrivMappingAPDefaultEntry.setStatus("current")


class _RuijieAPdefaultDSCPTag_Type(Integer32):
    """Custom type ruijieAPdefaultDSCPTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RuijieAPdefaultDSCPTag_Type.__name__ = "Integer32"
_RuijieAPdefaultDSCPTag_Object = MibTableColumn
ruijieAPdefaultDSCPTag = _RuijieAPdefaultDSCPTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 2, 1, 1),
    _RuijieAPdefaultDSCPTag_Type()
)
ruijieAPdefaultDSCPTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPdefaultDSCPTag.setStatus("current")
_RuijieAPdefaultDot1pTag_Type = Integer32
_RuijieAPdefaultDot1pTag_Object = MibTableColumn
ruijieAPdefaultDot1pTag = _RuijieAPdefaultDot1pTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 2, 2, 1, 2),
    _RuijieAPdefaultDot1pTag_Type()
)
ruijieAPdefaultDot1pTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPdefaultDot1pTag.setStatus("current")
_RuijieWlanDevicePrivMappingTableObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDevicePrivMappingTableObjects = _RuijieWlanDevicePrivMappingTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 3)
)
_RuijieSVPMappingTable_Object = MibTable
ruijieSVPMappingTable = _RuijieSVPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieSVPMappingTable.setStatus("current")
_RuijieSVPMappingEntry_Object = MibTableRow
ruijieSVPMappingEntry = _RuijieSVPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 3, 1, 1)
)
ruijieSVPMappingEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ruijieSVPMappingEntry.setStatus("current")


class _RuijieSVPmappingStatus_Type(Integer32):
    """Custom type ruijieSVPmappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_RuijieSVPmappingStatus_Type.__name__ = "Integer32"
_RuijieSVPmappingStatus_Object = MibTableColumn
ruijieSVPmappingStatus = _RuijieSVPmappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 3, 1, 1, 1),
    _RuijieSVPmappingStatus_Type()
)
ruijieSVPmappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSVPmappingStatus.setStatus("current")


class _RuijieSVPmappingAC_Type(Integer32):
    """Custom type ruijieSVPmappingAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("wmmvo", 1),
          ("wmmvi", 2),
          ("wmmbe", 3),
          ("wmmbk", 4))
    )


_RuijieSVPmappingAC_Type.__name__ = "Integer32"
_RuijieSVPmappingAC_Object = MibTableColumn
ruijieSVPmappingAC = _RuijieSVPmappingAC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 3, 3, 1, 1, 2),
    _RuijieSVPmappingAC_Type()
)
ruijieSVPmappingAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSVPmappingAC.setStatus("current")
_RuijieWlanDeviceRatelimitObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDeviceRatelimitObjects = _RuijieWlanDeviceRatelimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4)
)
_RuijieWlanRatelimitTable_Object = MibTable
ruijieWlanRatelimitTable = _RuijieWlanRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieWlanRatelimitTable.setStatus("current")
_RuijieWlanRatelimitEntry_Object = MibTableRow
ruijieWlanRatelimitEntry = _RuijieWlanRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 1, 1)
)
ruijieWlanRatelimitEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanRateLimitDirect"),
)
if mibBuilder.loadTexts:
    ruijieWlanRatelimitEntry.setStatus("current")


class _RuijieWlanRateLimitDirect_Type(Integer32):
    """Custom type ruijieWlanRateLimitDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanRateLimitDirect_Type.__name__ = "Integer32"
_RuijieWlanRateLimitDirect_Object = MibTableColumn
ruijieWlanRateLimitDirect = _RuijieWlanRateLimitDirect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 1, 1, 1),
    _RuijieWlanRateLimitDirect_Type()
)
ruijieWlanRateLimitDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanRateLimitDirect.setStatus("current")


class _RuijieWlanRatelimitStatus_Type(Integer32):
    """Custom type ruijieWlanRatelimitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanRatelimitStatus_Type.__name__ = "Integer32"
_RuijieWlanRatelimitStatus_Object = MibTableColumn
ruijieWlanRatelimitStatus = _RuijieWlanRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 1, 1, 2),
    _RuijieWlanRatelimitStatus_Type()
)
ruijieWlanRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanRatelimitStatus.setStatus("current")
_RuijieWlanAverageRate_Type = Integer32
_RuijieWlanAverageRate_Object = MibTableColumn
ruijieWlanAverageRate = _RuijieWlanAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 1, 1, 3),
    _RuijieWlanAverageRate_Type()
)
ruijieWlanAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanAverageRate.setStatus("current")
_RuijieWlanBurstRate_Type = Integer32
_RuijieWlanBurstRate_Object = MibTableColumn
ruijieWlanBurstRate = _RuijieWlanBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 1, 1, 4),
    _RuijieWlanBurstRate_Type()
)
ruijieWlanBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanBurstRate.setStatus("current")
_RuijieAPRatelimitTable_Object = MibTable
ruijieAPRatelimitTable = _RuijieAPRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 2)
)
if mibBuilder.loadTexts:
    ruijieAPRatelimitTable.setStatus("current")
_RuijieAPRatelimitEntry_Object = MibTableRow
ruijieAPRatelimitEntry = _RuijieAPRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 2, 1)
)
ruijieAPRatelimitEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPRateLimitDirect"),
)
if mibBuilder.loadTexts:
    ruijieAPRatelimitEntry.setStatus("current")


class _RuijieAPRateLimitDirect_Type(Integer32):
    """Custom type ruijieAPRateLimitDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAPRateLimitDirect_Type.__name__ = "Integer32"
_RuijieAPRateLimitDirect_Object = MibTableColumn
ruijieAPRateLimitDirect = _RuijieAPRateLimitDirect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 2, 1, 1),
    _RuijieAPRateLimitDirect_Type()
)
ruijieAPRateLimitDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAPRateLimitDirect.setStatus("current")


class _RuijieAPRatelimitStatus_Type(Integer32):
    """Custom type ruijieAPRatelimitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAPRatelimitStatus_Type.__name__ = "Integer32"
_RuijieAPRatelimitStatus_Object = MibTableColumn
ruijieAPRatelimitStatus = _RuijieAPRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 2, 1, 2),
    _RuijieAPRatelimitStatus_Type()
)
ruijieAPRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPRatelimitStatus.setStatus("current")
_RuijieAPAverageRate_Type = Integer32
_RuijieAPAverageRate_Object = MibTableColumn
ruijieAPAverageRate = _RuijieAPAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 2, 1, 3),
    _RuijieAPAverageRate_Type()
)
ruijieAPAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPAverageRate.setStatus("current")
_RuijieAPBurstRate_Type = Integer32
_RuijieAPBurstRate_Object = MibTableColumn
ruijieAPBurstRate = _RuijieAPBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 2, 1, 4),
    _RuijieAPBurstRate_Type()
)
ruijieAPBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAPBurstRate.setStatus("current")
_RuijieUserRatelimitTable_Object = MibTable
ruijieUserRatelimitTable = _RuijieUserRatelimitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 3)
)
if mibBuilder.loadTexts:
    ruijieUserRatelimitTable.setStatus("current")
_RuijieUserRatelimitEntry_Object = MibTableRow
ruijieUserRatelimitEntry = _RuijieUserRatelimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 3, 1)
)
ruijieUserRatelimitEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
    (0, "RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieUserRateLimitDirect"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ruijieUserRatelimitEntry.setStatus("current")


class _RuijieUserRateLimitDirect_Type(Integer32):
    """Custom type ruijieUserRateLimitDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieUserRateLimitDirect_Type.__name__ = "Integer32"
_RuijieUserRateLimitDirect_Object = MibTableColumn
ruijieUserRateLimitDirect = _RuijieUserRateLimitDirect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 3, 1, 1),
    _RuijieUserRateLimitDirect_Type()
)
ruijieUserRateLimitDirect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieUserRateLimitDirect.setStatus("current")


class _RuijieUserRatelimitStatus_Type(Integer32):
    """Custom type ruijieUserRatelimitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieUserRatelimitStatus_Type.__name__ = "Integer32"
_RuijieUserRatelimitStatus_Object = MibTableColumn
ruijieUserRatelimitStatus = _RuijieUserRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 3, 1, 2),
    _RuijieUserRatelimitStatus_Type()
)
ruijieUserRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUserRatelimitStatus.setStatus("current")
_RuijieUserAverageRate_Type = Integer32
_RuijieUserAverageRate_Object = MibTableColumn
ruijieUserAverageRate = _RuijieUserAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 3, 1, 3),
    _RuijieUserAverageRate_Type()
)
ruijieUserAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUserAverageRate.setStatus("current")
_RuijieUserBurstRate_Type = Integer32
_RuijieUserBurstRate_Object = MibTableColumn
ruijieUserBurstRate = _RuijieUserBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 4, 3, 1, 4),
    _RuijieUserBurstRate_Type()
)
ruijieUserBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUserBurstRate.setStatus("current")
_RuijieWlanQosMIBConform_ObjectIdentity = ObjectIdentity
ruijieWlanQosMIBConform = _RuijieWlanQosMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5)
)
_RuijieWlanQosMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieWlanQosMIBCompliances = _RuijieWlanQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5, 1)
)
_RuijieWlanQosMIBGroups_ObjectIdentity = ObjectIdentity
ruijieWlanQosMIBGroups = _RuijieWlanQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5, 2)
)

# Managed Objects groups

ruijieWlanQosWMMEDCAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5, 2, 1)
)
ruijieWlanQosWMMEDCAConfigGroup.setObjects(
      *(("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWMMStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPSDStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieSMPSStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieQAPEDCAqueuedepth"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieQAPEDCAcacPolicy"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieQAPEDCAcacParam"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanDefualtACnum"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanMaxstadot1ptag"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot1pmappingstatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedscpmappingstatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPdefaultDSCPTag"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPdefaultDot1pTag"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableCWmin"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableCWmax"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableAIFSN"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableTXOPLimit"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableMSDULifetime"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11EDCATableMandatory"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableCWmin"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableCWmax"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableAIFSN"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableTXOPLimit"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableMSDULifetime"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijiedot11QAPEDCATableMandatory"))
)
if mibBuilder.loadTexts:
    ruijieWlanQosWMMEDCAConfigGroup.setStatus("current")

ruijieWlanQosRatelimitConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5, 2, 2)
)
ruijieWlanQosRatelimitConfigGroup.setObjects(
      *(("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanRateLimitDirect"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanRatelimitStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanAverageRate"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanBurstRate"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPRatelimitStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPAverageRate"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieAPBurstRate"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieUserRatelimitStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieUserAverageRate"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieUserBurstRate"))
)
if mibBuilder.loadTexts:
    ruijieWlanQosRatelimitConfigGroup.setStatus("current")

ruijieWlanQosPriMappingonfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5, 2, 3)
)
ruijieWlanQosPriMappingonfigGroup.setObjects(
      *(("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieSVPmappingStatus"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieSVPmappingAC"))
)
if mibBuilder.loadTexts:
    ruijieWlanQosPriMappingonfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieWlanQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 60, 5, 1, 1)
)
ruijieWlanQosMIBCompliance.setObjects(
      *(("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanQosWMMEDCAConfigGroup"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanQosRatelimitConfigGroup"),
        ("RUIJIE-WLAN-QOS-EXTRA-MIB", "ruijieWlanQosPriMappingonfigGroup"))
)
if mibBuilder.loadTexts:
    ruijieWlanQosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-QOS-EXTRA-MIB",
    **{"ruijieWlanQosExtraMib": ruijieWlanQosExtraMib,
       "ruijieWlanDeviceWMMObjects": ruijieWlanDeviceWMMObjects,
       "ruijieWMMStatusTable": ruijieWMMStatusTable,
       "ruijieWMMStatusEntry": ruijieWMMStatusEntry,
       "ruijieWMMStatus": ruijieWMMStatus,
       "ruijieAPSDStatus": ruijieAPSDStatus,
       "ruijieSMPSStatus": ruijieSMPSStatus,
       "ruijieWlanDeviceEDCAObjects": ruijieWlanDeviceEDCAObjects,
       "ruijiedot11EDCATable": ruijiedot11EDCATable,
       "ruijiedot11EDCAEntry": ruijiedot11EDCAEntry,
       "ruijiedot11EDCATableIndex": ruijiedot11EDCATableIndex,
       "ruijiedot11EDCATableCWmin": ruijiedot11EDCATableCWmin,
       "ruijiedot11EDCATableCWmax": ruijiedot11EDCATableCWmax,
       "ruijiedot11EDCATableAIFSN": ruijiedot11EDCATableAIFSN,
       "ruijiedot11EDCATableTXOPLimit": ruijiedot11EDCATableTXOPLimit,
       "ruijiedot11EDCATableMSDULifetime": ruijiedot11EDCATableMSDULifetime,
       "ruijiedot11EDCATableMandatory": ruijiedot11EDCATableMandatory,
       "ruijiedot11QAPEDCATable": ruijiedot11QAPEDCATable,
       "ruijiedot11QAPEDCAEntry": ruijiedot11QAPEDCAEntry,
       "ruijiedot11QAPEDCATableIndex": ruijiedot11QAPEDCATableIndex,
       "ruijiedot11QAPEDCATableCWmin": ruijiedot11QAPEDCATableCWmin,
       "ruijiedot11QAPEDCATableCWmax": ruijiedot11QAPEDCATableCWmax,
       "ruijiedot11QAPEDCATableAIFSN": ruijiedot11QAPEDCATableAIFSN,
       "ruijiedot11QAPEDCATableTXOPLimit": ruijiedot11QAPEDCATableTXOPLimit,
       "ruijiedot11QAPEDCATableMSDULifetime": ruijiedot11QAPEDCATableMSDULifetime,
       "ruijiedot11QAPEDCATableMandatory": ruijiedot11QAPEDCATableMandatory,
       "ruijieWlanEDCATable": ruijieWlanEDCATable,
       "ruijieEDCAStatusEntry": ruijieEDCAStatusEntry,
       "ruijieQAPEDCAqueuedepth": ruijieQAPEDCAqueuedepth,
       "ruijieQAPEDCAcacPolicy": ruijieQAPEDCAcacPolicy,
       "ruijieQAPEDCAcacParam": ruijieQAPEDCAcacParam,
       "ruijieWlanDevicePrivMappingObjects": ruijieWlanDevicePrivMappingObjects,
       "ruijieWlanDevicePrivMappingWlanDefaultObjects": ruijieWlanDevicePrivMappingWlanDefaultObjects,
       "ruijieWlanDefaultACTable": ruijieWlanDefaultACTable,
       "ruijieWlanDefaultACEntry": ruijieWlanDefaultACEntry,
       "ruijieWlanDefualtACnum": ruijieWlanDefualtACnum,
       "ruijieWlanMaxstadot1ptag": ruijieWlanMaxstadot1ptag,
       "ruijieWlanDevicePrivMappingAPDefaultObjects": ruijieWlanDevicePrivMappingAPDefaultObjects,
       "ruijiePrivMappingAPstatusTable": ruijiePrivMappingAPstatusTable,
       "ruijieAPdefaultStatusMappingEntry": ruijieAPdefaultStatusMappingEntry,
       "ruijiedot1pmappingstatus": ruijiedot1pmappingstatus,
       "ruijiedscpmappingstatus": ruijiedscpmappingstatus,
       "ruijiePrivMappingAPDefaultTable": ruijiePrivMappingAPDefaultTable,
       "ruijiePrivMappingAPDefaultEntry": ruijiePrivMappingAPDefaultEntry,
       "ruijieAPdefaultDSCPTag": ruijieAPdefaultDSCPTag,
       "ruijieAPdefaultDot1pTag": ruijieAPdefaultDot1pTag,
       "ruijieWlanDevicePrivMappingTableObjects": ruijieWlanDevicePrivMappingTableObjects,
       "ruijieSVPMappingTable": ruijieSVPMappingTable,
       "ruijieSVPMappingEntry": ruijieSVPMappingEntry,
       "ruijieSVPmappingStatus": ruijieSVPmappingStatus,
       "ruijieSVPmappingAC": ruijieSVPmappingAC,
       "ruijieWlanDeviceRatelimitObjects": ruijieWlanDeviceRatelimitObjects,
       "ruijieWlanRatelimitTable": ruijieWlanRatelimitTable,
       "ruijieWlanRatelimitEntry": ruijieWlanRatelimitEntry,
       "ruijieWlanRateLimitDirect": ruijieWlanRateLimitDirect,
       "ruijieWlanRatelimitStatus": ruijieWlanRatelimitStatus,
       "ruijieWlanAverageRate": ruijieWlanAverageRate,
       "ruijieWlanBurstRate": ruijieWlanBurstRate,
       "ruijieAPRatelimitTable": ruijieAPRatelimitTable,
       "ruijieAPRatelimitEntry": ruijieAPRatelimitEntry,
       "ruijieAPRateLimitDirect": ruijieAPRateLimitDirect,
       "ruijieAPRatelimitStatus": ruijieAPRatelimitStatus,
       "ruijieAPAverageRate": ruijieAPAverageRate,
       "ruijieAPBurstRate": ruijieAPBurstRate,
       "ruijieUserRatelimitTable": ruijieUserRatelimitTable,
       "ruijieUserRatelimitEntry": ruijieUserRatelimitEntry,
       "ruijieUserRateLimitDirect": ruijieUserRateLimitDirect,
       "ruijieUserRatelimitStatus": ruijieUserRatelimitStatus,
       "ruijieUserAverageRate": ruijieUserAverageRate,
       "ruijieUserBurstRate": ruijieUserBurstRate,
       "ruijieWlanQosMIBConform": ruijieWlanQosMIBConform,
       "ruijieWlanQosMIBCompliances": ruijieWlanQosMIBCompliances,
       "ruijieWlanQosMIBCompliance": ruijieWlanQosMIBCompliance,
       "ruijieWlanQosMIBGroups": ruijieWlanQosMIBGroups,
       "ruijieWlanQosWMMEDCAConfigGroup": ruijieWlanQosWMMEDCAConfigGroup,
       "ruijieWlanQosRatelimitConfigGroup": ruijieWlanQosRatelimitConfigGroup,
       "ruijieWlanQosPriMappingonfigGroup": ruijieWlanQosPriMappingonfigGroup}
)
