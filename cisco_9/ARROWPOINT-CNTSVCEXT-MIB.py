# SNMP MIB module (ARROWPOINT-CNTSVCEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ARROWPOINT-CNTSVCEXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 19:35:05 2025
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

(cntsvcExt,) = mibBuilder.importSymbols(
    "CISCO-APENT-MIB",
    "cntsvcExt")

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

(RowStatus,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "RowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApCntsvcExtMib_ObjectIdentity = ObjectIdentity
apCntsvcExtMib = _ApCntsvcExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1)
)
_ApCntsvcExtMibNotifs_ObjectIdentity = ObjectIdentity
apCntsvcExtMibNotifs = _ApCntsvcExtMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 0)
)
_ApCntsvcExtMibObjects_ObjectIdentity = ObjectIdentity
apCntsvcExtMibObjects = _ApCntsvcExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 1)
)
_ApCntsvcExtMibConform_ObjectIdentity = ObjectIdentity
apCntsvcExtMibConform = _ApCntsvcExtMibConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 2)
)
_ApCntsvcExtMibCompliances_ObjectIdentity = ObjectIdentity
apCntsvcExtMibCompliances = _ApCntsvcExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 2, 1)
)
_ApCntsvcExtMibCompliance_ObjectIdentity = ObjectIdentity
apCntsvcExtMibCompliance = _ApCntsvcExtMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 2, 1, 1)
)
_ApCntsvcExtMibGroups_ObjectIdentity = ObjectIdentity
apCntsvcExtMibGroups = _ApCntsvcExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 2, 2)
)
_ApCntsvcExtMibGroup_ObjectIdentity = ObjectIdentity
apCntsvcExtMibGroup = _ApCntsvcExtMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 2, 2, 1)
)
_ApCntsvcExtDeprecatedMibGroup_ObjectIdentity = ObjectIdentity
apCntsvcExtDeprecatedMibGroup = _ApCntsvcExtDeprecatedMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 1, 2, 2, 2)
)
_ApCntsvcTable_Object = MibTable
apCntsvcTable = _ApCntsvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2)
)
if mibBuilder.loadTexts:
    apCntsvcTable.setStatus("mandatory")
_ApCntsvcEntry_Object = MibTableRow
apCntsvcEntry = _ApCntsvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1)
)
apCntsvcEntry.setIndexNames(
    (0, "ARROWPOINT-CNTSVCEXT-MIB", "apCntsvcOwnName"),
    (0, "ARROWPOINT-CNTSVCEXT-MIB", "apCntsvcCntName"),
    (0, "ARROWPOINT-CNTSVCEXT-MIB", "apCntsvcSvcName"),
)
if mibBuilder.loadTexts:
    apCntsvcEntry.setStatus("mandatory")


class _ApCntsvcOwnName_Type(SnmpAdminString):
    """Custom type apCntsvcOwnName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntsvcOwnName_Type.__name__ = "SnmpAdminString"
_ApCntsvcOwnName_Object = MibTableColumn
apCntsvcOwnName = _ApCntsvcOwnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 1),
    _ApCntsvcOwnName_Type()
)
apCntsvcOwnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntsvcOwnName.setStatus("mandatory")


class _ApCntsvcCntName_Type(SnmpAdminString):
    """Custom type apCntsvcCntName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntsvcCntName_Type.__name__ = "SnmpAdminString"
_ApCntsvcCntName_Object = MibTableColumn
apCntsvcCntName = _ApCntsvcCntName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 2),
    _ApCntsvcCntName_Type()
)
apCntsvcCntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntsvcCntName.setStatus("mandatory")


class _ApCntsvcSvcName_Type(SnmpAdminString):
    """Custom type apCntsvcSvcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntsvcSvcName_Type.__name__ = "SnmpAdminString"
_ApCntsvcSvcName_Object = MibTableColumn
apCntsvcSvcName = _ApCntsvcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 3),
    _ApCntsvcSvcName_Type()
)
apCntsvcSvcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntsvcSvcName.setStatus("mandatory")
_ApCntsvcHits_Type = Counter32
_ApCntsvcHits_Object = MibTableColumn
apCntsvcHits = _ApCntsvcHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 4),
    _ApCntsvcHits_Type()
)
apCntsvcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcHits.setStatus("mandatory")
_ApCntsvcBytes_Type = Counter32
_ApCntsvcBytes_Object = MibTableColumn
apCntsvcBytes = _ApCntsvcBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 5),
    _ApCntsvcBytes_Type()
)
apCntsvcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcBytes.setStatus("mandatory")
_ApCntsvcFrames_Type = Counter32
_ApCntsvcFrames_Object = MibTableColumn
apCntsvcFrames = _ApCntsvcFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 6),
    _ApCntsvcFrames_Type()
)
apCntsvcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcFrames.setStatus("mandatory")


class _ApCntsvcBucket_Type(Integer32):
    """Custom type apCntsvcBucket based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ApCntsvcBucket_Type.__name__ = "Integer32"
_ApCntsvcBucket_Object = MibTableColumn
apCntsvcBucket = _ApCntsvcBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 7),
    _ApCntsvcBucket_Type()
)
apCntsvcBucket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntsvcBucket.setStatus("mandatory")
_ApCntsvcStatus_Type = RowStatus
_ApCntsvcStatus_Object = MibTableColumn
apCntsvcStatus = _ApCntsvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 8),
    _ApCntsvcStatus_Type()
)
apCntsvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntsvcStatus.setStatus("mandatory")


class _ApCntsvcWeight_Type(Integer32):
    """Custom type apCntsvcWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ApCntsvcWeight_Type.__name__ = "Integer32"
_ApCntsvcWeight_Object = MibTableColumn
apCntsvcWeight = _ApCntsvcWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 9),
    _ApCntsvcWeight_Type()
)
apCntsvcWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCntsvcWeight.setStatus("mandatory")
_ApCntsvcDnsHits_Type = Counter32
_ApCntsvcDnsHits_Object = MibTableColumn
apCntsvcDnsHits = _ApCntsvcDnsHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 10),
    _ApCntsvcDnsHits_Type()
)
apCntsvcDnsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcDnsHits.setStatus("mandatory")
_ApCntsvcDnsProximityHits_Type = Counter32
_ApCntsvcDnsProximityHits_Object = MibTableColumn
apCntsvcDnsProximityHits = _ApCntsvcDnsProximityHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 11),
    _ApCntsvcDnsProximityHits_Type()
)
apCntsvcDnsProximityHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcDnsProximityHits.setStatus("mandatory")


class _ApCntsvcState_Type(Integer32):
    """Custom type apCntsvcState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("suspended", 1),
          ("down", 2),
          ("alive", 4))
    )


_ApCntsvcState_Type.__name__ = "Integer32"
_ApCntsvcState_Object = MibTableColumn
apCntsvcState = _ApCntsvcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 12),
    _ApCntsvcState_Type()
)
apCntsvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcState.setStatus("mandatory")


class _ApCntsvcDFPState_Type(Integer32):
    """Custom type apCntsvcDFPState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApCntsvcDFPState_Type.__name__ = "Integer32"
_ApCntsvcDFPState_Object = MibTableColumn
apCntsvcDFPState = _ApCntsvcDFPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 13),
    _ApCntsvcDFPState_Type()
)
apCntsvcDFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcDFPState.setStatus("deprecated")


class _ApCntsvcDFPWeight_Type(Integer32):
    """Custom type apCntsvcDFPWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntsvcDFPWeight_Type.__name__ = "Integer32"
_ApCntsvcDFPWeight_Object = MibTableColumn
apCntsvcDFPWeight = _ApCntsvcDFPWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 14),
    _ApCntsvcDFPWeight_Type()
)
apCntsvcDFPWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcDFPWeight.setStatus("deprecated")


class _ApCntsvcReportedWeightSource_Type(Integer32):
    """Custom type apCntsvcReportedWeightSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dfp", 2),
          ("sasp", 3))
    )


_ApCntsvcReportedWeightSource_Type.__name__ = "Integer32"
_ApCntsvcReportedWeightSource_Object = MibTableColumn
apCntsvcReportedWeightSource = _ApCntsvcReportedWeightSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 15),
    _ApCntsvcReportedWeightSource_Type()
)
apCntsvcReportedWeightSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcReportedWeightSource.setStatus("mandatory")


class _ApCntsvcReportedWeight_Type(Gauge32):
    """Custom type apCntsvcReportedWeight based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApCntsvcReportedWeight_Type.__name__ = "Gauge32"
_ApCntsvcReportedWeight_Object = MibTableColumn
apCntsvcReportedWeight = _ApCntsvcReportedWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 18, 2, 1, 16),
    _ApCntsvcReportedWeight_Type()
)
apCntsvcReportedWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcReportedWeight.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARROWPOINT-CNTSVCEXT-MIB",
    **{"apCntsvcExtMib": apCntsvcExtMib,
       "apCntsvcExtMibNotifs": apCntsvcExtMibNotifs,
       "apCntsvcExtMibObjects": apCntsvcExtMibObjects,
       "apCntsvcExtMibConform": apCntsvcExtMibConform,
       "apCntsvcExtMibCompliances": apCntsvcExtMibCompliances,
       "apCntsvcExtMibCompliance": apCntsvcExtMibCompliance,
       "apCntsvcExtMibGroups": apCntsvcExtMibGroups,
       "apCntsvcExtMibGroup": apCntsvcExtMibGroup,
       "apCntsvcExtDeprecatedMibGroup": apCntsvcExtDeprecatedMibGroup,
       "apCntsvcTable": apCntsvcTable,
       "apCntsvcEntry": apCntsvcEntry,
       "apCntsvcOwnName": apCntsvcOwnName,
       "apCntsvcCntName": apCntsvcCntName,
       "apCntsvcSvcName": apCntsvcSvcName,
       "apCntsvcHits": apCntsvcHits,
       "apCntsvcBytes": apCntsvcBytes,
       "apCntsvcFrames": apCntsvcFrames,
       "apCntsvcBucket": apCntsvcBucket,
       "apCntsvcStatus": apCntsvcStatus,
       "apCntsvcWeight": apCntsvcWeight,
       "apCntsvcDnsHits": apCntsvcDnsHits,
       "apCntsvcDnsProximityHits": apCntsvcDnsProximityHits,
       "apCntsvcState": apCntsvcState,
       "apCntsvcDFPState": apCntsvcDFPState,
       "apCntsvcDFPWeight": apCntsvcDFPWeight,
       "apCntsvcReportedWeightSource": apCntsvcReportedWeightSource,
       "apCntsvcReportedWeight": apCntsvcReportedWeight}
)
