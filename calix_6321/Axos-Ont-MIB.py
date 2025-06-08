# SNMP MIB module (Axos-Ont-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/Axos-Ont-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:18:56 2025
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

(axosModules,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "axosModules")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

axosOntModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    axosOntModule.setRevisions(
        ("2020-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxosOntTable_Object = MibTable
axosOntTable = _AxosOntTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    axosOntTable.setStatus("current")
_AxosOntEntry_Object = MibTableRow
axosOntEntry = _AxosOntEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1)
)
axosOntEntry.setIndexNames(
    (0, "Axos-Ont-MIB", "axosOntIndex"),
)
if mibBuilder.loadTexts:
    axosOntEntry.setStatus("current")
_AxosOntIndex_Type = Integer32
_AxosOntIndex_Object = MibTableColumn
axosOntIndex = _AxosOntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 1),
    _AxosOntIndex_Type()
)
axosOntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axosOntIndex.setStatus("current")
_AxosOntID_Type = OctetString
_AxosOntID_Object = MibTableColumn
axosOntID = _AxosOntID_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 2),
    _AxosOntID_Type()
)
axosOntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntID.setStatus("current")


class _AxosOntAdminStatus_Type(Integer32):
    """Custom type axosOntAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_AxosOntAdminStatus_Type.__name__ = "Integer32"
_AxosOntAdminStatus_Object = MibTableColumn
axosOntAdminStatus = _AxosOntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 3),
    _AxosOntAdminStatus_Type()
)
axosOntAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntAdminStatus.setStatus("current")


class _AxosOntOperStatus_Type(Integer32):
    """Custom type axosOntOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enabled", 1),
          ("degraded", 2))
    )


_AxosOntOperStatus_Type.__name__ = "Integer32"
_AxosOntOperStatus_Object = MibTableColumn
axosOntOperStatus = _AxosOntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 4),
    _AxosOntOperStatus_Type()
)
axosOntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntOperStatus.setStatus("current")


class _AxosOntDyingGasp_Type(Integer32):
    """Custom type axosOntDyingGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("no", 0),
          ("yes", 1))
    )


_AxosOntDyingGasp_Type.__name__ = "Integer32"
_AxosOntDyingGasp_Object = MibTableColumn
axosOntDyingGasp = _AxosOntDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 5),
    _AxosOntDyingGasp_Type()
)
axosOntDyingGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntDyingGasp.setStatus("current")
_AxosOntRxOpticalLevel_Type = Integer32
_AxosOntRxOpticalLevel_Object = MibTableColumn
axosOntRxOpticalLevel = _AxosOntRxOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 6),
    _AxosOntRxOpticalLevel_Type()
)
axosOntRxOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntRxOpticalLevel.setStatus("current")
_AxosOntTxOpticalLevel_Type = Integer32
_AxosOntTxOpticalLevel_Object = MibTableColumn
axosOntTxOpticalLevel = _AxosOntTxOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 7),
    _AxosOntTxOpticalLevel_Type()
)
axosOntTxOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntTxOpticalLevel.setStatus("current")
_AxosOntFarEndRxOpticalLevel_Type = Integer32
_AxosOntFarEndRxOpticalLevel_Object = MibTableColumn
axosOntFarEndRxOpticalLevel = _AxosOntFarEndRxOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 8),
    _AxosOntFarEndRxOpticalLevel_Type()
)
axosOntFarEndRxOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntFarEndRxOpticalLevel.setStatus("current")
_AxosOntSoftwareVersion_Type = OctetString
_AxosOntSoftwareVersion_Object = MibTableColumn
axosOntSoftwareVersion = _AxosOntSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 9),
    _AxosOntSoftwareVersion_Type()
)
axosOntSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntSoftwareVersion.setStatus("current")
_AxosOntCleiCode_Type = OctetString
_AxosOntCleiCode_Object = MibTableColumn
axosOntCleiCode = _AxosOntCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 4, 2, 6, 1, 1, 10),
    _AxosOntCleiCode_Type()
)
axosOntCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axosOntCleiCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Axos-Ont-MIB",
    **{"axosOntModule": axosOntModule,
       "axosOntTable": axosOntTable,
       "axosOntEntry": axosOntEntry,
       "axosOntIndex": axosOntIndex,
       "axosOntID": axosOntID,
       "axosOntAdminStatus": axosOntAdminStatus,
       "axosOntOperStatus": axosOntOperStatus,
       "axosOntDyingGasp": axosOntDyingGasp,
       "axosOntRxOpticalLevel": axosOntRxOpticalLevel,
       "axosOntTxOpticalLevel": axosOntTxOpticalLevel,
       "axosOntFarEndRxOpticalLevel": axosOntFarEndRxOpticalLevel,
       "axosOntSoftwareVersion": axosOntSoftwareVersion,
       "axosOntCleiCode": axosOntCleiCode}
)
